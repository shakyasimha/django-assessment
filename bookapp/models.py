from django.db import models

# Create your models here.
class Book(models.Model):
    ## Book model
    ## Fields in the model:
    ## title (char)
    ## author  (char)
    ## publication year -> pub_year (int)
    def __init__(self):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=200)
        pub_year = models.IntegerField(default=0)
