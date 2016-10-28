from django.db import models
from hashids import Hashids

# Create your models here.

class Bookmark(models.Model):
    full_url = models.URLField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def encode(self):
        hashids = Hashids().encode((self.id + 1000000))
        return hashids

    def click_count(self):
        return Click.objects.filter(user=self.user).filter(bookmark=self.id).count()


    class Meta:
        ordering = ("-created", )

class Click(models.Model):
    user = models.ForeignKey('auth.User')
    bookmark = models.ForeignKey('app.Bookmark')
    timestamp = models.DateTimeField(auto_now_add=True)
    value = models.BooleanField()

    def __str__(self):
        return "{} - {}".format(self.bookmark, self.timestamp)
