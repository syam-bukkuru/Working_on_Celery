from django.shortcuts import render
from myceleryproject.celery import add
from myapp.task import sub
from celery.result import AsyncResult

# Create your views here.
def index(request):
    res = add.delay(10, 20)
    print('result : ', res)
    res1 = sub.delay(10, 20)
    print('result : ', res1)
    return render(request, 'home.html' ,{'res' : res})

def check_task(request, task_id):
    res = AsyncResult(task_id)
    return render(request, 'result.html', {'res' : res})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')