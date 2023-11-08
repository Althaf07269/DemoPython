from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import task
from .forms import taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


# Create your views here.

class tasklistview(ListView):
    model=task
    template_name='home.html'
    context_object_name = 'task1'

class taskdetailview(DetailView):
    model=task
    template_name='detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model=task
    template_name='update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')


    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail', kwargs={'pk': self.object.id})



class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')

def add(request):
    task1=task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        Task=task(name=name,priority=priority,date=date)
        Task.save()
    return render(request,"home.html",{'task1':task1})
def delete(request,id):
    if request.method =='POST':
        tasks = task.objects.get(id=id)
        tasks.delete()
        return redirect('/')
    return render(request, "delete.html")
def update(request,id1):
    task2=task.objects.get(id=id1)
    form=taskform(request.POST or None,instance=task2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'task':task2})
