from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    #check if requset method is POST or GET
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        #Authonticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In")
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect('home')
    else:
        return render(request, 'home.html',{})

# def login_user(request):
#    pass

def logout_user(request):
    pass