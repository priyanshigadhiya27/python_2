from django.db import models

class Python(models.Model):
    name=models.CharField()
    score=models.IntegerField()
    sub=models.CharField()
    
    def __str__(self):
        return self.name
