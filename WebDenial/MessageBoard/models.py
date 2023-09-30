from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.conf import settings

from django.conf import settings
User = settings.AUTH_USER_MODEL

class MyProfileManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must supply an email")
        if not username:
            raise ValueError("Users must supply a username")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self.db)
        return user

class Profile(AbstractUser, PermissionsMixin):
    #We can add more, but base user has stuff
    objects = MyProfileManager()
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=40, unique=True) 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login =  models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    posts = models.OneToOneField('Post',on_delete=models.PROTECT, null=True)

    USERNAME_FIELD = 'username'

    
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]
    
    title = models.TextField()
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
