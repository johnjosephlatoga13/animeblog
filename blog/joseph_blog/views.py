from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Comment
from .forms import BlogForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

def index(request):    
	template = 'blog_list.html'    
	blogs = Blog.objects.all()    
	context = {         
		'blogs': blogs,    
	}    
	return render(request, template, context)

def add_blog(request):
	
	template = "add_blog.html"

	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			fs= form.save(commit=False)
			fs.author= request.user.username
			fs.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
				'blog_form': BlogForm(),
		}
	return render(request, template, context)

def edit_blog(request, blog_id):
	
	template = "edit_blog.html"
	blog = Blog.objects.get(id=int(blog_id))

	if request.method == "POST":
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			# fs= form.save(commit=False)
			# fs.author= request.user.username
			form.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
				'blog_form': BlogForm(instance=blog),
		}
	return render(request, template, context)	

def view_comment(request, comment_id):

	template = "view_comment.html"
	blog = Blog.objects.get(id=int(comment_id))
	comments = Comment.objects.all().filter(blog_title=int(comment_id))
	context = {
		'comments':comments,
		'blog':blog
    }

	return render(request, template, context)

def add_comment(request, blog_id):
	
	template = "add_comment.html"
	blog = Blog.objects.get(id=int(blog_id))

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			fs= form.save(commit=False)
			fs.author= request.user.username
			fs.blog_title= blog_id
			fs.save()
			return HttpResponseRedirect(reverse_lazy('blog:index'))
	else:
		context = {
				'comment_form': CommentForm(),
				'blog':blog
		}
	return render(request, template, context)		

def delete_comment(request, comment_id):
	comment = Comment.objects.get(id=int(comment_id))
	comment.delete()
	return HttpResponseRedirect(reverse_lazy('blog:index'))		