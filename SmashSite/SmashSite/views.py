from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

def index(request):
    template_name = 'SmashSite/index.html'
    return render(request, template_name)

def register(request):
    #gets user input in form, checks input, and creates new user
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'SmashSite/index.html')
    context = {
        "form": form,
    }
    return render(request, 'SmashSite/register.html', context)

def login_user(request):
    #checks user input against database and logs in user if valid
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'SmashSite/index.html')
            else:
                return render(request, 'SmashSite/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'SmashSite/login.html', {'error_message': 'Invalid login'})
    return render(request, 'SmashSite/login.html')

def user_logout(request):
    #logs out user
    logout(request)
    return render(request, 'SmashSite/index.html')
