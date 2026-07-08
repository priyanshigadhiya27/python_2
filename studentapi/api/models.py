from django.db import models

class Course(models.Model):
    course=models.CharField()
    duration=models.IntegerField()

    def __str__(self):
        return self.course
    
class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='student')
    name=models.CharField()
    age=models.IntegerField()

    def __str__(self):
        return self.name