from django.contrib import admin

# Register your models here.
from products.models import Product, Color, Category, Sku


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'is_active']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    fields = ['name', 'is_active']


class SkuInline(admin.TabularInline):
    model = Sku
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'status', 'is_active']
    inlines = [SkuInline]


