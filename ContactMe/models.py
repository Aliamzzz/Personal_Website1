from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')

    def __str__(self):
        return self.name

class Message(models.Model):
    firstName = models.CharField(max_length=100, blank=False, null=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return f"{self.firstName} {self.lastName} | {self.email}"
