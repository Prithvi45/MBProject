from django.db import models

# Create your models here.


class DummyData(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()

