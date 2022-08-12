from django import forms
from .models import Comment, Post, Contact


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
