from django import forms
from django.db import models


class Input(models.Model):
    text = models.TextField()
    #result = models.CharField()#choices=["suicide"]

    def __str__(self):
        return '%s' % (self.text)