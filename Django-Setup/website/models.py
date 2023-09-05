from django.db import models

# Create your models here.

class Repo_Block(models.Model):
    course_name = models.TextField()
    department = models.TextField()
    repo = models.TextField()
    semester = models.TextField()
    prereqs = models.TextField() 
