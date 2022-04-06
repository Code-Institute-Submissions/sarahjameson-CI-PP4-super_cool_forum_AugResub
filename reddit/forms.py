# from xml.etree.ElementTree import Comment
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('body',)
