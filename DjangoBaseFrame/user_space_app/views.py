from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def userSpace(request):
	return render(request,'user_space_app/user_space.html')