from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime 

class Category(models.Model):
    name1= models.CharField(max_length=100)

    def __str__(self):
        return self.name1

class Post(models.Model):
    class PostObjects(models.Model):
        def get_queryset(self):
            return super().get_queryset().filter(status='published') ##selects all the posts that has status 'published'
    options=(
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    category= models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )   ##We do not want to delete all the psots in a category on deleting that category...
      ##so that if anyone tries to delete any category, it has no effects on the posts related to that category
    title=models.CharField(max_length=250)
    excerpt= models.TextField(null=True)
    content= models.TextField()
    slug=models.SlugField(max_length=250, unique_for_date='unpublished')

    
    published= models.DateTimeField(auto_now=True)

    author= models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    ) ##author is another foreign key to the User table imported on the top and if
    ##we delete any user, it is going to delete the posts they made..
    status= models.CharField(max_length=10, choices=options, default='published')
    objects= models.Manager() #default manager
    postobjects= PostObjects() #custom manager

    class Meta:
        ordering= ('-published',) ##we want to arrange data in descending order based upon the published date
    
    def __str__(self):
        return self.titile

