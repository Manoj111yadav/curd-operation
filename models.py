from django.db import models

class User(models.Model):   #applicatio name model class name crudApp_User
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=20)
    address=models.CharField(max_length=20)