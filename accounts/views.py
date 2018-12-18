from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


def signup(request):
    # User wishes to signup and has submitted relevant information.
    if request.method == 'POST':
        # Retrieves user input.
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']

        if password == password_check:
            try:
                # A user with that username already exists. Send the user an error.
                User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {'error': 'Username already exists!'})
            except User.DoesNotExist:
                # No user exits, create user successfully and bring them to the home page.
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                return redirect('clinical/home')
        else:
            # User failed to enter two passwords that matched.
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match!'})

    # Displays sign up page.
    return render(request, 'accounts/signup.html')


def login(request):
    # User wants to login.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # User was able to be logged in successful. Sends them to the home page.
            auth.login(request, user)
            return redirect('clinical/home')
        else:
            # Either the username or password was incorrect. This sends them back to the login page.
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})

    # Displays login page.
    return render(request, 'accounts/login.html')


def logout(request):
    # Logs the user out of their account and brings them back to the home page.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


