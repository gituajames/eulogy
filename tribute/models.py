from django.db import models


class TributeMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

# Create your models here.
