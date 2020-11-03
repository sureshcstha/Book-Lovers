from django.db import models


# Create your models here.
class Book(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rating = models.FloatField()
    image = models.ImageField(upload_to='images', default='images/none/noimg.jpg')

