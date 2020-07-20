from django.db import models



# Create your models here.

class Pra(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name