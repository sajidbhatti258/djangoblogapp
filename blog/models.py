from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)  # Automatically convert name to slug
        # Ensure uniqueness of the slug
        if Category.objects.filter(slug=self.slug).exists():
            self.slug = f"{slugify(self.name)}-{Category.objects.filter(slug__startswith=self.slug).count()}"
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content =  HTMLField()
    post_image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.title)
            unique_slug = slug_base
            # Ensure the slug is unique
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug_base}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
