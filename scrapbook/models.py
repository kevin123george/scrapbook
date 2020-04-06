from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.datetime_safe import date
from django_extensions.db.fields import AutoSlugField


class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = AutoSlugField('slug', populate_from='title', unique=True)
    publication_date = models.DateField(default=date.today)


