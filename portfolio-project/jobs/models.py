from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary

class Blog(models.Model):
    # Title
    title = models.CharField(max_length=200)
    # Body
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title