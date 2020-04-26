from django.contrib import admin

# Register your models here.
from products.models import Product, Color, Category, Sku


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


class SkuInline(admin.TabularInline):
    model = Sku
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [SkuInline]


