from django.contrib import admin
from .models import Category, Product
from parler.admin import TranslatableAdmin

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
#class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #prepopulated_fields = {'slug': ('name',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
#class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    #prepopulated_fields = {'slug': ('name',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}