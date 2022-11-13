from django import forms
from django.db import models


class Input(models.Model):
    text = models.TextField()
    result = models.CharField(auto_created=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.text, self.result)