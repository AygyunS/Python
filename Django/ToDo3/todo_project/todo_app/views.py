from django.shortcuts import render
from .models import Task
from .forms import TaskForm


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'todo_app/list_tasks.html', {'tasks': tasks})
