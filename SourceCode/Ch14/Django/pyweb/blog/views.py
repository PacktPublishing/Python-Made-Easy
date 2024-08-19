from datetime import datetime  # Importing the datetime module from the Python standard library
from django.shortcuts import render, redirect  # Importing necessary functions for rendering templates and redirecting
from blog.forms import PostForm  # Importing the 'PostForm' form from the 'blog' app's forms.py
from blog.models import Post  # Importing the 'Post' model from the 'blog' app's models.py

def create_post(request):
    if request.method == 'POST':  # Checking if the request method is 'POST'
        form = PostForm(request.POST)  # Creating a form instance with the submitted data
        if form.is_valid():  # Checking if the form data is valid
            post = form.save(commit=False)  # Saving the form data to a new 'Post' object without committing to the database yet
            post.pub_date = datetime.now()  # Setting the 'pub_date' attribute of the post to the current datetime
            post.save()  # Saving the post object to the database
            return redirect('post_list')  # Redirecting the user to the 'post_list' URL
    else:
        form = PostForm()  # Creating a new empty instance of the 'PostForm'

    return render(request, 'blog/create_post.html', {'form': form})  # Rendering the 'create_post' template with the form data


def post_list(request):
    posts = Post.objects.all()  # Retrieving all 'Post' objects from the database
    return render(request, 'blog/post_list.html', {'posts': posts})  # Rendering the 'post_list' template with the retrieved posts

