from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    lastname = models.CharField(max_length = 255)
    age = models.IntegerField()
    phone = models.CharField(max_length = 12)

    def __str__(self):
        return self.name

class Pet(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150)
    age = models.IntegerField()
    person = models.ForeignKey(Person, on_delete = models.CASCADE)

    def __str__(self):
        return self.name