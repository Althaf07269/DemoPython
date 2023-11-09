from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Movie
from .forms import Movieform
# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'cinema': movie
    }
    return render(request,"index.html",context)
def detail(request,mid):
    m=Movie.objects.get(id=mid)
    return render(request,"detail.html",{'c':m})

def add_movie(request):
    if request.method=='POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img= request.FILES['img']
        movie=Movie(name=name,des=des,year=year,img=img)
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html")

