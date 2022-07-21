from .models import Comment, Post, Contact
from django import forms


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
        fields = '__all__'
