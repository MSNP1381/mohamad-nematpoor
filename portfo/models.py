from django.db import models


class porto(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image= models.ImageField(upload_to='potrfo/image/')
    url = models.URLField(blank=True)
    date=models.DateTimeField()