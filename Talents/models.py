from django.db import models

class Talent(models.Model):
    name = models.CharField(max_length=100)
    mastery = models.IntegerField()

    def __str__(self):
        return self.name