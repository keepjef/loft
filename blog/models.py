from django.db import models
from autoslug import AutoSlugField

from slugify import slugify


class Theme(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('title', )
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        """Return title and username."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Theme, self).save(*args, **kwargs)


class Post(models.Model):
    """Post model."""
    title = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to='posts/photos')
    text = models.TextField(default=None, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, blank=False)
    themes = models.ManyToManyField(Theme, blank=True, null=True, related_name="themes")


    class Meta:
        ordering = ['-created']
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


    def __str__(self):
        """Return title and username."""
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)