from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    place = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.FileField()

    def __str__(self):
        return self.name
