from django.db import models
from .utils import slug_generator_name
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, primary_key=True, unique=True, blank=True)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slug_generator_name(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
