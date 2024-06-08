from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check kara chi k urername chi k nai
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            # return redirect('home')
        
        # Authenticate kara chi user na
        user = authenticate(username=username, password=password)
        
        if user is None:
            # Display kar sa error of possward wrong hasa to 
            messages.error(request, "Invalid Password")
            # return redirect('index')
        else:
            # password right hasa to login thi jasa
            auth_login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')  
    
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        conpassw = request.POST.get('conpassword')

        if passw != conpassw:
            messages.error(request, "Passwords do not match")
            return redirect('login')  

        if User.objects.filter(username=email).exists():
            messages.error(request, "User already exists")
            return redirect('login')

        user = User.objects.create_user(username=email, email=email, password=passw, first_name=fname, last_name=lname)
        auth_login(request, user)
        messages.success(request, "Account created successfully!")
        return redirect('login') 

    return render(request, 'signup.html')  # Ensure you have a separate signup.html template
