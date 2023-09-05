from django.db import models

# Create your models here.
class Fields(models.Model):
    field_1 = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    my_numeric_field = models.IntegerField()
