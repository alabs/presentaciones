from django.db import models
from datetime import datetime


class Book(models.Model):
    name = models.CharField(max_length=255)
    slug_name = models.SlugField(unique=True, help_text='nombre en la URL')
    author = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, editable=False)
    isbn = models.CharField(null=True, blank=True, max_length=20)

    def __unicode__(self):
        return self.name
