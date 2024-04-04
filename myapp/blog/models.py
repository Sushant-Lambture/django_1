from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=100)
    eloc=models.CharField(max_length=100)
    esal=models.IntegerField()
    def __str__(self):
        return self.ename


class Upload(models.Model):
    pid=models.AutoField
    pname=models.CharField(max_length=100)
    pcat=models.CharField(max_length=100)
    psubcat=models.CharField(max_length=100)
    pprice=models.IntegerField(default=0)
    pdate=models.DateField()
    pimage=models.ImageField(upload_to="blog/image",default="")
    # in pimage path is given only blog / image  because we have to mention it in myapp / settings using os
    def __str__(self):
        return  self.pname
