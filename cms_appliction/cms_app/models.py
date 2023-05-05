# Create your models here.
from django.db import models
from django.forms.models import model_to_dict

class User(models.Model):
    user_id  = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=250)
    content = models.TextField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)