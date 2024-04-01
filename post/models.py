from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

from user.models import Profile

class Tag(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    video = models.FileField(upload_to='posts/videos/', blank=True)
    description = models.TextField()
    likes = models.ManyToManyField(Profile, related_name='liked_posts', blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    upvote = models.ManyToManyField(Profile, related_name='upvoted_posts', blank=True)
    downvote = models.ManyToManyField(Profile, related_name='downvoted_posts', blank=True)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self._state.adding and self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            counter = 1
            original_slug = self.slug
            while self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='files/images/')
    added_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Using ContentType framework for generic relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Comment on {self.content_object}"

class CommentImage(models.Model):
    comment_image = models.ImageField(upload_to='files/comment_images/')
    added_time = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Report(models.Model):
    reported_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    reported_object_id = models.PositiveIntegerField(null=True)
    reported_post = GenericForeignKey('reported_content_type', 'reported_object_id')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
