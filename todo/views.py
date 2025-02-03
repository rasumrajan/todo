from django.shortcuts import redirect, render
from .models import Add_task
# Create your views here.
def ViewTask(request):
  task = request.POST['task']
  Add_task.objects.create(add_task=task)
  return redirect('home')