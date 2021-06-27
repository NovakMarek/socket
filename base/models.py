from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django import forms

class Task(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=16)
  description = models.TextField(max_length=175, null=True, blank=True)
  complete = models.BooleanField(default=False) #Tohle možná nebudu potřebovat
  created = models.DateTimeField(auto_now_add=True)
  blue = models.BooleanField(default=True) 
  red = models.BooleanField(default=False)
  orange = models.BooleanField(default=False)
  yellow = models.BooleanField(default=False)
  green = models.BooleanField(default=False)


  def __str__(self):
    return self.title
  

#sorting notes by
class Meta:
  ordering = ['created']


class SignUpForm(UserCreationForm):
  email = forms.EmailField()
  first_name = forms.CharField(max_length=50)
  last_name = forms.CharField(max_length=50)

  class Meta:
    model = User
    fields = ['username','first_name','last_name', 'email', 'password1','password2']
