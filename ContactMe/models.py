from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name
