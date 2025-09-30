from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
# Create your views here.


def home_page(request):
    incomplete_tasks = models.Todo.objects.filter(is_completed=False)
    completed_tasks = models.Todo.objects.filter(is_completed=True)
    context = {'incomplete_tasks': incomplete_tasks,
               'completed_tasks': completed_tasks}
    return render(request, "home_page.html", context=context)


def add_task(request):
    task = request.POST['task']
    models.Todo.objects.create(task=task)
    return redirect('home')


def remove_task(request, id):
    task = models.Todo.objects.get(pk=id)
    task.delete()
    return redirect('home')


def mark_as_done(request, id):
    task = models.Todo.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_done(request, id):
    task = models.Todo.objects.get(pk=id)
    task.is_completed = True
    task.save()
    return redirect('home')


def mark_as_undone(request, id):
    task = models.Todo.objects.get(pk=id)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, id):
    task = models.Todo.objects.get(pk=id)
    if request.method == "POST":
        task.task = request.POST['task']
        task.save()
        return redirect('home')
    else:
        context = {"task": task}
        return render(request, 'edit_task.html', context)
