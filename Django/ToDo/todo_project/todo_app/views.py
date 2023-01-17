from django.shortcuts import render, redirect
from .forms import TodoForm


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # Save the todo item to the database
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_app/add_todo.html', {'form': form})
