from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title