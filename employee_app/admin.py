from django.contrib import admin
from .models import EmployeeDetailsModel, ExperianceModel, TaskModel
# Register your models here.
# admin.site.register(EmployeeDetailsModel)
@admin.register(EmployeeDetailsModel)
class EmployeeDetailsModelAdmin(admin.ModelAdmin):
    list_display=['id','name','age','experiance','emp_id','id_card']
admin.site.register(ExperianceModel)
admin.site.register(TaskModel)

