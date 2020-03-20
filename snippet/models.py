from django.db import models
from users.models import User
from django.utils.text import slugify

class Snippet(models.Model):
    title = models.CharField(max_length=80)
    code = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    languages = models.ForeignKey('Language', on_delete=models.DO_NOTHING, null=True, blank=True)
    public = models.BooleanField(default=False)
    language = models.CharField(max_length=80)
    user = models.ForeignKey(to=User, default=None, null=True, 
                             on_delete=models.CASCADE,
                             related_name='snippets')
    def __str__(self):
        return f'{self.title}'

class Language(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)