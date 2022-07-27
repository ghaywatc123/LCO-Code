from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateTimeField

class Category(models.Model):
        name = models.CharField(max_length = 50)
        description = models.CharField(max_length = 50)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)

        def __str__(self) -> str:
            return self.name
