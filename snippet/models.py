from django.db import models
from users.models import User

class Snippet(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    lang = models.ForeignKey('Lang', on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='snippets')
    def __str__(self):
        return f'{self.title}'

class Lang(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)