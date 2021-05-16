from django import forms
from .models import CommentSection

class Comment_Section(forms.ModelForm):
     class Meta:
          model = CommentSection
          fields = ['name', 'email', 'comment']
          widgets = {
               'name': forms.TextInput(attrs={'class': 'comment-sec', 'placeholder': 'Name'}),
               'email': forms.TextInput(attrs={'class': 'comment-sec', 'placeholder': 'Email'}),
               'comment': forms.TextInput(attrs={'class': 'comment-sec', 'id':'body','placeholder': 'Add a Comment'})
          }