from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def userLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "There was an error Logging in, Try Again.")
            return redirect('user-login')
    else:
        return render(request, 'authentications/login.html', {})
    
def userLogout(request):
    logout(request)
    messages.success(request, "Logout Successfull!")
    return redirect('home')


def UserRegister(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful!'))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authentications/user_register.html', {'form': form})