from django.shortcuts import render, redirect
from django.views.generic import ListView
from Annotation.models import Vod, Post
from Annotation.forms import PostForm, VodForm
import datetime
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

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
    
def vod(request):
    #acquires 25 vods
    queryset = Vod.objects.all().order_by("-date")[:25]

    
    if request.method == "POST":
        form = VodForm(request.POST)
        user = request.user
        if user is not None:
            if form.is_valid():
                current_vod = form.save(commit=False)
                current_vod.user = user
                current_vod.save()
                return HttpResponseRedirect(reverse("Annotation-feed"))
            else:
                print(form.errors)
    else:     
        form = VodForm()
    context = {'object_list':queryset, 'form':form}

    return render(request, 'Annotation/home.html', context)

def vote(request,vkey, key):
    user = request.user
    #retrieves specific post
    try:
        target_post = Post.objects.get(pk=int(key))
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    if user is not None:
        #retrieve all the posts that this user has voted on
        if target_post.votes.exists(user.id):
            target_post.votes.down(user.id)
        else:
            target_post.votes.up(user.id)
        target_post.vote_count = target_post.votes.count()
        target_post.save()
            
    return redirect(post, key=int(vkey))
            
    
