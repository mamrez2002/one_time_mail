from django.db import models

import secrets
# Create your models here.



class Mail(models.Model):
    text = models.TextField()
    auth = models.CharField(max_length=200  , unique=True)

    def __str__(self):
        return self.auth[0:10]
