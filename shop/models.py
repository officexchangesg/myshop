from django.db import models
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.apps import apps
from parler.models import TranslatableModel, TranslatedFields

name = apps.get_app_config('shop').name
media_storage = fs = FileSystemStorage(location=name + '/media')


media_path = apps.get_app_config('shop').name + "/media"
media_storage = fs = FileSystemStorage(location=media_path)


# class Category(models.Model):
#     name = models.CharField(max_length=200,
#                             db_index=True)
#     slug = models.SlugField(max_length=200,
#                             unique=True)
class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200,
                                db_index=True),
        slug = models.SlugField(max_length=200,
                                db_index=True,
                                unique=True)
    )

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

    class Meta:
        # ordering = ('name',)   #comment out due to parler
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name

# class Product(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     description = models.TextField(blank=True)

class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        description = models.TextField(blank=True)
    )
    category = models.ForeignKey(Category,
            related_name='products',
            on_delete=models.CASCADE)
    image = models.ImageField(storage=media_storage,upload_to='products/%Y/%m/%d',
                              blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
