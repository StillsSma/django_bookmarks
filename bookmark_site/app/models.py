from django.db import models
from hashids import Hashids

# Create your models here.

class Bookmark(models.Model):
    full_url = models.URLField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return self.title

    def encode(self):
        hashids = Hashids().encode((self.id + 1000000))
        return hashids


    class Meta:
        ordering = ("-created", )
