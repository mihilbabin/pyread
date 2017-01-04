from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, db_index=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pages:detail', args=[self.slug])

class Page(models.Model):
    category = models.ForeignKey(Category, related_name='pages')
    title = models.CharField(max_length=120)
    url = models.URLField()
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
