from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, HttpResponseServerError
from django.template import loader
from django.conf import settings
from django.views.decorators import gzip
from django.views.decorators.csrf import csrf_exempt
import json
import os
from django.http import FileResponse
from .models import IPTables
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages

# from channels.generic.websocket import WebsocketConsumer





def logout(request):
    '''Handle logout view'''

    auth.logout(request)
    return redirect('login')


def login(request):
    '''define views for login page'''

    print('Login called')
    template = loader.get_template('login.html')
    return HttpResponse(template.render({"": ""}, request))


def user_authenticate(request):

    print('User authenticate', request.method)
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            # Return an error message
            return render(request, 'login.html', {'form': {}, 'error_message': 'Invalid login credentials'})
    else:
        # Return an error message
        return render(request, 'login.html', {'form': {}, 'error_message': 'Invalid login credentials'})


@login_required(login_url='login')
def index(request):
    template = loader.get_template('index.html')

    data = {"message": "Welcome"}
    return HttpResponse(template.render(data, request))


def signup_action(request) : 

    template  = loader.get_template("signup.html")
    return HttpResponse(template.render({},request))

def signup(request):
    if request.method == 'POST':
        # Get the form data
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            error_message = 'This username is already taken'
            return render(request, 'signup.html', {'error_message': error_message})
        
        # Check if the email is already in use
        if User.objects.filter(email=email).exists():
            error_message = 'This email address already exists'
            return render(request, 'signup.html', {'error_message': error_message})
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

         # Add a success message
        messages.success(request, ' account has been created successfully. Please log in.')
        
        
        # Redirect the user to the login page
        return redirect('login')
        # # Redirect the user to the login page with query parameter
        # return redirect('login' + '?created=true')
    
    
    # If the request method is not POST, just render the form
    return render(request, 'signup.html')