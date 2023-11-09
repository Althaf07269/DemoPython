from django.shortcuts import render
from .models import place
from .models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    context = {
        'result': obj,
        'team2': obj1
    }
    return render(request,'index.html',context)
















# def addition(request):
#     x=int(request.GET['num1'])
#     y =int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{"addition":res})

# def contact(request):
#     return HttpResponse("helo how are you")