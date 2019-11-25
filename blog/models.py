from django.db import models
import markdown


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    md = models.FileField(null=True)
    content = models.TextField(default="default")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        file = self.md
        decoded = file.read().decode('utf-8')
        extensions = ['fenced_code',
                      'codehilite']
        output = markdown.markdown(decoded, extensions=extensions)
        self.content = output

        super().save(*args, **kwargs)
