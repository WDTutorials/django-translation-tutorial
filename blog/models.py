from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    body = models.TextField(blank=False, default='')
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', default='')
    image_thumbnail = ImageSpecField(source='image',
                                  processors=[Thumbnail(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def __str__(self):
        return self.title
