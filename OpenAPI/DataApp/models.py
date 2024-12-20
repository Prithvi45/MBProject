from django.db import models

# Create your models here.


class DummyData(models.Model):
    #name = models.CharField(max_length=100)
    ten_min_std_deviation = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    ten_min_sampled_avg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    time = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    datetime = models.DateTimeField()

