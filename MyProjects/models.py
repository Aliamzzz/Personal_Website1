from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    shortDescription = models.CharField(max_length=100, blank=True, null=True)
    fullDescription = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='projects_images/')
    link = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=100, blank=True, null=True)
    tools = models.CharField(max_length=200, blank=True, null=True)



    def __str__(self):
        return self.name