from django.db import models

# Create your models here.
class Blog_Content(models.Model):
    title =models.CharField(max_length=100)
    url = models.URLField(blank=True)
    decrip1 = models.TextField(default='لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.')
    timestamp=models.DateTimeField()
    def __str__(self):
     return self.title
