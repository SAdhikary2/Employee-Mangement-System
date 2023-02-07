from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=50)

    def __str__(self):
         return self.name

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)

    
    def __str__(self):
        return self.name


class Employee(models.Model):
    First_Name=models.CharField(max_length=100,null=False)
    Last_Name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonus=models.IntegerField(default=0)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    phone=models.IntegerField(default=0)
    hiring_date=models.DateField()

    
    def __str__(self):
        return "%s %s %s"%(self.First_Name,self.Last_Name,self.phone)
