from django.contrib import admin
from .models import EmployeeDetailsModel
# Register your models here.
# admin.site.register(EmployeeDetailsModel)
@admin.register(EmployeeDetailsModel)
class EmployeeDetailsModelAdmin(admin.ModelAdmin):
    list_display=['id','name','age','experiance','emp_id','id_card']

