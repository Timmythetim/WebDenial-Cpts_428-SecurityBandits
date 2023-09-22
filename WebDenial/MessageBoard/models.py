from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.user.get_username()
    
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)

# TODO keep working on this guy
# https://realpython.com/python-django-blog/#create-the-django-blog-application