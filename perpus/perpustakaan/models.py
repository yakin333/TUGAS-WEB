from django.db import models

# Create your models here.
class tambak(models.Model):
    nama = models.CharField(max_length=100)


    def __str__(self):
        return self.nama