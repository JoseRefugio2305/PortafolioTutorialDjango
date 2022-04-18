from distutils.command.upload import upload
from django.db import models
import datetime
#cada clase es un modelo, cada una de ellas vendria a ser un tabla en la bdd
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/img')
    date = models.DateField(datetime.date.today)
