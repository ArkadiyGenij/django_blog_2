from django.db import models
from django.urls import reverse


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, null=True, blank=True, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview_image = models.ImageField(upload_to='preview/%Y/%m/%d', null=True, blank=True, verbose_name='превью')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
