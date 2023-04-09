from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=80, null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}, {self.location}'

class Role(models.Model):
    name = models.CharField(max_length=80, null=False)
    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    f_name = models.CharField(max_length=80, null=False)
    l_name = models.CharField(max_length=80)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()
    bonus = models.FloatField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return f'{self.f_name}, {self.l_name}, {self.dept}, {self.salary}'