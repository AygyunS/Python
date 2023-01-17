from django.shortcuts import render, redirect
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        if title:
            task = Task(title=title)
            task.save()
        return redirect('/')
    return render(request, 'tasks/add.html')


def edit(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()
        return redirect('/')
    return render(request, 'tasks/edit.html', {'task': task})
