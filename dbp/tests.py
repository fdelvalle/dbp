from django.test import TestCase
from django.utils.text import slugify


class ModelTests(TestCase):

    def test_create_category(self):
        from products.models import Category
        category = Category(name="Categoria 1")
        category.save()
        self.assertIn(category.slug, slugify(category.name))

    def test_create_product(self):
        from products.models import Category, Product
        category = Category.objects.create(name="Categoria 1")
        product = Product.objects.create(name='Product 1', category=category)
        self.assertIn(product.name, product.__str__())

    def test_create_color(self):
        from products.models import Color
        color = Color(name="Red")
        color.save()
        self.assertIn(color.slug, 'red')

    def test_create_sku(self):
        from products.models import Category, Product, Color, Sku
        category = Category.objects.create(name="Categoria 1")
        product = Product.objects.create(name='Product 1', category=category)
        color = Color.objects.create(name="Blue")
        sku, created = Sku.objects.get_or_create(product=product, color=color, size=1)
        self.assertIs(created, True)
