from django.shortcuts import render

# Create your views here.
def app2_vista(request): 
    return render(request,'home.html')