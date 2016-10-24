from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User

def profile(request, key):
    try:
        target_user = User.objects.get(pk=int(key))
    except User.DoesNotExist:
        raise Http404("User does not exist")

    #this retrieves all the comments the user has posted
    user_posts = target_user.post_set.all().order_by("-date")
    #need to get the vods of these posts
    vods = []
    for post in user_posts:
        #post.vod_set.all() should return a queryset with one vod
        #to access object within queryset, must iterate through it
        current_vod = post.vod_set.all()
        for vod in current_vod:
            if vod not in vods:
                vods.append(vod)
    
    #this retrieves all the vods the user has posted
    user_vods = target_user.vod_set.all().order_by("-date")

    #context = {'user': target_user, 'total_list': total_list, 'user_vods':user_vods}
    context = {'user': target_user, 'vods_list' : vods, 'user_vods':user_vods}
    return render(request, 'Profile/home.html', context)
