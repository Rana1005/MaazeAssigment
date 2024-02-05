from django.db import models

# Create your models here.
class EmployeeDetailsModel(models.Model):
    def namefile(instance,filename):
        return '/'.join(["idproof/",str(instance.name),filename])
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    experiance = models.IntegerField()
    emp_id = models.CharField(max_length = 100, null = True, blank = True)
    id_card = models.FileField(upload_to=namefile)

    def save(self, *args, **kwargs):
        self.emp_id = "Maaze"+"__"+self.name
        super(EmployeeDetailsModel, self).save(*args, **kwargs)

class ExperianceModel(models.Model):
    employee = models.ForeignKey(EmployeeDetailsModel, on_delete=models.CASCADE)
    organation = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    salary = models.CharField(max_length = 100)

class TaskModel(models.Model):
    employee = models.ForeignKey(EmployeeDetailsModel, on_delete=models.CASCADE)
    taskname = models.CharField(max_length = 100)
    required_time = models.CharField(max_length = 100)
    manager = models.CharField(max_length = 100)

    
    

