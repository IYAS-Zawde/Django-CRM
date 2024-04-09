from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

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
    logout(request)
    messages.success(request, "You've been logged out successfully")
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def register_user_2(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authonticate and loging
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username= username, password = password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered Well Done!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
        
    return render(request, 'register.html', {'form':form})