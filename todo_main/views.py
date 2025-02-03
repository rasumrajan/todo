
from django.shortcuts import render

from todo.models import Add_task


def home(request):
   task = Add_task.objects.filter(is_completed = False).order_by('-updated_at')
   context = {
      'task' : task,
   }
   return render(request,'home.html',context)