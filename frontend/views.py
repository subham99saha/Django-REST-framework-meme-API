from django.shortcuts import render

# Create your views here.
def frontEnd(request):
	return render(request, 'home.html')