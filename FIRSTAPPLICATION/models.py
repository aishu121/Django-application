from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return '{}.format(self.name)'

class ID(models.Model):
    id = models.IntegerField(primary_key=True)

class Contact(models.Model):
    contact = models.CharField(max_length=100)

class Address(models.Model):
    address = models.TextField()


    

