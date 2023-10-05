from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import TaskForm

from .models import *


# Create your views here.

def list(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)
	print("********************+")

	if request.method == 'POST':
		print("sdfssfg")
		form = TaskForm(request.POST or None, instance=task)
		print("++++++++++++++++")
		if form.is_valid():
			form.save()
            
		return redirect('/')

	context = {'form':form}
	
	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)

