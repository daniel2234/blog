from django.db import models

# Create your models here.

# many to one relationship, this means automatically that a given user can be the autohr of many different  blog post but not the other way around
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