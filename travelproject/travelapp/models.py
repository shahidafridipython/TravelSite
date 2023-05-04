from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='pics')
    Description=models.TextField()

    def __str__(self):
        return self.name

class member(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to='photo')
    description1=models.TextField()

    def __str__(self):
        return self.name1