from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import UserSignUpForm

def signUp(request):
	if request.method == 'POST':
		form = UserSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('login_page')
	else:
		form = UserSignUpForm()

	return render(request, 'user_access_app/signup.html', {'form': form, 'title': 'Sign Up!'})

def login(request):
	return render(request,'user_access_app/login.html')

def logout(request):
	return render(request,'user_access_app/logout.html')