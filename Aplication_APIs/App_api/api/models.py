from django.db import models

# Create your models here.
class App(models.Model):
    app_name = models.CharField(max_length=105)
    version = models.CharField(max_length=105)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.app_name