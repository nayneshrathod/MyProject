from django.shortcuts import render

# Create your views here.
def index(request):
    res = " Naynesh "
    return render(request,'index.html',{"data":res})
