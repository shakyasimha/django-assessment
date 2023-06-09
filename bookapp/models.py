from django.db import models
from django.utils import timezone 

# Create your models here.
class Book(models.Model):
    ## Book model
    ## Fields in the model:
    ## title (char)
    ## author  (char)
    ## publication year -> pub_year (int)
    title    = models.CharField(max_length=200)
    author   = models.CharField(max_length=200)
    pub_year = models.IntegerField(default=timezone.now())
    

    # Constructor
    """
    def __init__(self, title, author, pub_year):
        self.title    = title 
        self.author   = author 
        self.pub_year = pub_year
    """   