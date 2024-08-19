from django import forms  # Importing the forms module from Django
from blog.models import Post  # Importing the 'Post' model from the 'blog' app's models.py

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Specifies that the form is based on the 'Post' model
        fields = ['title', 'content']  # Specifies the fields to include in the form


