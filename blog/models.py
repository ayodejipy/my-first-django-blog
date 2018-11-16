from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    def saveCategory(self):
        self.created = timezone.now()
        self.save()

    def __str__(self):
        return self.title