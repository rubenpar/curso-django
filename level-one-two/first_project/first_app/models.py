from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharFiled(max_lenght=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage (models.Model):
    
