from django.conf.urls import url
from .views import *

urlpatterns = [    
	url(r'^$', index, name='index'),
	url(r'^add_blog$', add_blog, name='add-blog'),
	url(r'^edit_blog/(?P<blog_id>\d+)$', edit_blog, name='edit-blog'),
	url(r'^view_comment/(?P<comment_id>\d+)$', view_comment, name='view-comment'),
	# url(r'^add_comment$', add_comment, name='add-comment'),
	url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
	url(r'^add_comment/(?P<blog_id>\d+)$', add_comment, name='add-comment'),
]