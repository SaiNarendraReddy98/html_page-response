from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')

def secound(request):
    return render(request,'secound.html')
