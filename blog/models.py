from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return f'name {self.name}'

