from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		# fields = "__all__"

		CHOICES = (
					( 1, "One Piece"),
					( 2, "Naruto"),
					( 3, "Bleach"),
					( 4, "My Hero Academia"),
					( 5, "Seven Deadly Sin"),
					( 6, "Others...")
				)
		fields = ('title', 'body', 'anime_title', 'author')
		# username = request.user.username
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'id':'', 'type':'hidden'}),
			# 'datetime': forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
			'anime_title': forms.Select(choices=CHOICES),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		# fields = "__all__"

		
		fields = ('author', 'blog_title', 'body')
		# blog_title = forms.IntegerField()
		# body = forms.CharField(widget=forms.Textarea(attrs={'size': '1000'}))
		# username = request.user.username
		widgets = {
			'blog_title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}),
			'body': forms.TextInput(attrs={'class': 'form-control'}),
			# 'author': forms.TextInput(attrs={'class': 'form-control', 'id':'', 'type':'hidden'}),
		}		