from django.db import models

class Players(models.Model):
    name=models.CharField(max_length=50)
    runs=models.IntegerField()
    profile=models.URLField(max_length=200)
    email=models.EmailField(max_length=250)
    dob=models.DateField(blank=True)

    def __str__(self):
        return self.name  
       

