from django.db import models
from django.urls import reverse #new

# Create your models here.

# many to one relationship, this means automatically that a given user can be the author of many different  blog post but not the other way around
# the refernece is to the built-in User model that Django provides for authentication
#For all many-to-one relationships such as a ForeignKey we must also specify on on_delete option 
class Post(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(
    'auth.User',
    on_delete=models.CASCADE,
  )
  body = models.TextField()

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', args=[str(self.id)])



# Reverse provides us to reference an object by its URL template name, in this case post_detail, if you recall, our URL pattern is the following:

# That means in order for this route to work we must also pass in an argument with the pk(primary key) of the object
# pk and id are interchangable in Django though the Dnango cods recommned using self.id with get_absolute_url
#So we're telling Django that the ultimate location of a Post entry is its post_detail view which is posts /<int:pk>/ so the route for the first entry we've made will be at posts/1

