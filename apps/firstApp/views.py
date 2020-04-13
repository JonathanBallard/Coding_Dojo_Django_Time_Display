from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time.html',context)

def time_display(request):
    return redirect('/')