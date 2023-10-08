from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import NewUserForm, LoginForm
from django.contrib.auth import views, login, authenticate
from django.contrib import messages

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/placement/")
        
	form = NewUserForm()
	return render (request=request, template_name="signup.html", context={"form":form})


def login_request(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/placement/')
        ...
    else:
        print('hello')
        # Return an 'invalid login' error message.
        ...
    form = LoginForm()
    return render (request=request, template_name="login.html", context={"form":form})