from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)