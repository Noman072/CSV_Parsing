from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files')

   

class myfile(models.Model):
    Emp_id=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    year=models.CharField(max_length=29)
    domain=models.CharField(max_length=100)
    industry=models.CharField(max_length=100)
    size=models.CharField(max_length=10)
    area=models.CharField(max_length=500)


