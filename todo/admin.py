from django.contrib import admin
from .models import Add_task
# Register your models here.

class Show_col(admin.ModelAdmin):
  list_display =('add_task','is_completed','updated_at')

admin.site.register(Add_task,Show_col)