from django.shortcuts import render

# Create your views here.
def startPage(request):
	return render(request,'start_page_app/start_page.html')