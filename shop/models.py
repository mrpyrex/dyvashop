from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
# Create your models here.
class Category(models.Model):
    name        = models.CharField(max_length=250, db_index=True)
    slug        = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    name            = models.CharField(max_length=250, db_index=True)
    slug            = models.SlugField(db_index=True)
    image           = models.ImageField(upload_to='products/', blank=True)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    stock           = models.PositiveIntegerField()
    available       = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateField(auto_now=True)


    class Meta:
        ordering    = ('-created',)
        index_together  = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)