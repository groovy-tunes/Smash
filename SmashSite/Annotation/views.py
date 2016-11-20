from django.shortcuts import render, redirect
from django.views.generic import ListView
from Annotation.models import Vod, Post
from Annotation.forms import PostForm, VodForm
import datetime
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
import math

def post(request, key):
    #retrieves the specific vod object
    try:
        target_vod = Vod.objects.get(pk=int(key))
    except Vod.DoesNotExist:
        raise Http404("Vod does not exist")

    #handles commenting
    if request.method == "POST" and 'comment' in request.POST:
        form = PostForm(request.POST)
        user = request.user
        if user is not None:
            if form.is_valid():
                current_post = form.save(commit=False)
                current_post.user = user
                current_post.save()
                target_vod.posts.add(current_post)
                return HttpResponseRedirect(reverse("Annotation-post",args=[key]))
            else:
                print(form.errors)
                
    #loads the form for input if not POST
    else:          
        form = PostForm()

    #using vod object, retrieves all its posts and renders
    target_posts = Vod.objects.get(pk=int(key)).posts.all().order_by("-date")
    context = {'target_vod': target_vod, 'target_posts': target_posts, 'form':form}

    return render(request, 'Annotation/post.html', context)
    
def vod(request, page):
    #acquires 24 vods
    page = int(page)
    start = page * 24
    end = start + 24
    queryset = Vod.objects.all().order_by("-date")[start:end]

    
    if request.method == "POST":
        form = VodForm(request.POST)
        user = request.user
        if user is not None:
            if form.is_valid():
                current_vod = form.save(commit=False)
                current_vod.user = user
                current_vod.save()
                return HttpResponseRedirect(reverse("Annotation-feed", kwargs={'page':0}))
            else:
                print(form.errors)
    else:     
        form = VodForm()

    #used to determine whether to display pages
    pages = Vod.objects.all().count()
    previous = False
    after = False
    if (page - 1) >= 0:
        previous = True
    if pages > (page + 1) * 24:
        after = True
    
    context = {'object_list':queryset, 'form':form, 'page':page, 'previous':previous, 'after':after}

    return render(request, 'Annotation/home.html', context)

def vote(request,vkey, key):
    user = request.user
    #retrieves specific post
    try:
        target_post = Post.objects.get(pk=int(key))
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    if user is not None:
        #user can only upvote or remove previous vote
        if target_post.votes.exists(user.id):
            target_post.votes.down(user.id)
        else:
            target_post.votes.up(user.id)
        target_post.vote_count = target_post.votes.count()
        target_post.save()
            
    return redirect(post, key=int(vkey))
            
def delete(request, vkey, key):
    user = request.user
    try:
        target_post = Post.objects.get(pk=int(key))
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    if user is not None:
        target_post.delete()

    return redirect(post, key=int(vkey))
        
def delete_vod(request, vkey):
    user = request.user
    try:
        target_vod = Vod.objects.get(pk=int(vkey))
    except Vod.DoesNotExist:
        raise Http404("Vod does not exist")

    if user is not None:
        all_posts = target_vod.posts.all()
        all_posts.delete()
        target_vod.delete()

    return redirect("Annotation-feed", page=0)

def search(request, search_text):
    search_vods = Vod.objects.filter(title__contains=search_text).order_by("-date")
    form = VodForm()
    context = {'object_list':search_vods, 'form':form}
    
    return render(request, 'Annotation/search.html', context)
    
