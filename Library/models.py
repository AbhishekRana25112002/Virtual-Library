from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime


User=get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='book-icon.png')
    location= models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="post_images")
    title=models.CharField(unique=True,max_length=100)
    subtitle=models.CharField(max_length=200)
    content=models.TextField(blank=False)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    comment=models.TextField(blank=False)
    date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=255)
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    book = models.FileField(upload_to='books')
    image= models.ImageField(upload_to='books')
    category=models.CharField(max_length=100)
    about=models.TextField(blank=False)
    uploaded_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    book=models.ForeignKey(Books, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    comment=models.TextField(blank=False)
    date=models.DateField(default=datetime.now)

    def __str__(self):
        return self.name