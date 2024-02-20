from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=100)
    eloc=models.CharField(max_length=100)
    esal=models.IntegerField()
    def __str__(self):
        return self.ename