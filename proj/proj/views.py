from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def Home(request):
    return render(request,"home.html")

def aboutt(request):
    return render(request,'aboutus.html')

def term(request):
    return render(request,'term.html')