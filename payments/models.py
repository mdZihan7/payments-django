from django.db import models

# Create your models here.
class Payment(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length = 20)
    pemail = models.EmailField(max_length = 40)