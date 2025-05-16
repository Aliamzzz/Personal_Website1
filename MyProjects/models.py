from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects_images/')
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.name