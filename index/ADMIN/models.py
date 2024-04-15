from django.db import models

# Create your models here.
class Admin_account(models.Model):
    email = models.CharField(primary_key=True,max_length=250)
    passwd = models.CharField(max_length=100,null = False)

