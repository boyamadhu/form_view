from django.db import models
from django.core import validators
from django import forms
# Create your models here.

def sname_valid(value):
    if value[0].islower():
        raise forms.ValidationError('first character must in capital')
class Student(models.Model):
    sname=models.CharField(max_length=100,validators=[validators.RegexValidator('[A-Z]\w+')])
    sid=models.IntegerField(primary_key=True,validators=[])

        

    def __str__(self) -> str:
        return self.sname
