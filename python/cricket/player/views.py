from django.shortcuts import render,get_object_or_404
from player.models import Players
def home(request):
    player=Players.objects.all()
    return render(request,'home.html',{"player":player})
def about(request):
    return render(request,'about.html')

def info(request,id):
    play=get_object_or_404(Players,id)
    return render(request,"info.html",{"play":play})
    

