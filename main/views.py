from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html',context)
def ProJectView(request):
    context={}
    return render(request,'main/ProJect.html',context)

def language(request):
    context={}
    return render(request,'main/lan.html',context)