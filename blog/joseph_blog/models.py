from django.db import models

# Create your models here.
class Blog(models.Model):
	ANIME_TITLE = (
		( 1, "One Piece"),
		( 2, "Naruto"),
		( 3, "Bleach"),
		( 4, "My Hero Academia"),
		( 5, "Seven Deadly Sin"),
		( 6, "Others...")
	)	
	title = models.CharField(verbose_name="Title", max_length=500)
	body = models.CharField(verbose_name="Body", max_length=1000)
	author = models.CharField(verbose_name="Author", max_length=100, blank=True) 
	anime_title = models.IntegerField(verbose_name="Anime", choices=ANIME_TITLE)
	# datetime = models.DateTimeField()
	def __str__(self):
	    return "%s" % self.title	

	def __str__(self):
		return self.get_anime_title_display() 

class Comment(models.Model):
	# blog_title = models.ForeignKey(Blog, verbose_name="Blog Title",on_delete = models.CASCADE)
	blog_title = models.CharField(verbose_name="Blog Title", max_length=100, blank=True)
	body = models.CharField(verbose_name="Body", max_length=1000)
	author = models.CharField(verbose_name="Author", max_length=100, blank=True) 
	# datetime = models.DateTimeField()	 
	# def __str__(self):
	#     return "%s" % self.blog_title	