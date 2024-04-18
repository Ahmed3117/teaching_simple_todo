from django.shortcuts import redirect, render
from .models import Todo
# Create your views here.

def todos(request):
    todos = Todo.objects.all()
    # todos = Todo.objects.filter(is_complete=False)
    context={
        'todos':todos,
        }
    return render(request, 'todo/todos.html',context)

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect("todo:todos")

def update_todo(request,pk):
    print(pk)
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        new_title = request.POST.get('title')
        if new_title:
            todo.title = new_title
            todo.save()
            return redirect("todo:todos")
    context = {'todo': todo}
    return render(request, 'todo/update_todo.html',context)

def delete_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("todo:todos")

def edit_status_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    # if todo.is_complete == False:
    #     todo.is_complete = True
    # else:
    #     todo.is_complete = False
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect("todo:todos")