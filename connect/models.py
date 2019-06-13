from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Foundation(models.Model):
    image = models.ImageField(upload_to='foundation_pics',blank=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    website_link = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name  

class Awareness(models.Model):
    article_title = models.CharField(max_length=255)
    article = models.TextField()
    date = models.DateField(auto_now_add=True)
    foundation = models.ForeignKey(Foundation,blank=True)

    def __str__(self):
        return self.article_title

class Forums(models.Model):
    forum_title = models.CharField(max_length=255)
    forum_post = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_user = models.ForeignKey(User,blank=True)

    def __str__(self):
        return self.forum_title

    @classmethod
    def get_posts(cls):
        posts = Forums.objects.all()
        return posts

    class Meta:
        ordering = ['-id']

class Profile(models.Model):
    username = models.ForeignKey(User,blank=True)
    tel_no = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    user_location = models.CharField(max_length=255)

    def __str__(self):
        return self.user_location

class Comment(models.Model):
    user_comment = models.ForeignKey(User)
    comment = models.TextField()
    comment_id = models.IntegerField(default=0)

    def __str__(self):
        return self.comment
