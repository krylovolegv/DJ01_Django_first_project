from django.shortcuts import render

def home(request):
	return render(request, 'myapp/new_index.html')