from django.urls import path

from todo import views

urlpatterns = [
    path('addTask/',views.ViewTask,name='viewTask'),
]
