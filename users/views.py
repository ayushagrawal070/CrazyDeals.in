from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created for {username}! You can now Log in')
			return redirect('http://127.0.0.1:8000/login/')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')