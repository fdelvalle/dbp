from django.db import models

# Create your models here.
from dbp.models import BaseMixin
from dbp.utils import slugify_save


class Category(BaseMixin):
    name = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False, db_index=True, unique=True)
    slug = models.SlugField(verbose_name="slug", max_length=50, null=False, blank=False, db_index=True, unique=True)
    slug.pre_save = slugify_save

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


PRODUCT_STATUS = (
    (1, 'INATIVO'),
    (2, 'ATIVO')
)


class Product(BaseMixin):
    name = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False, db_index=True, unique=True)
    slug = models.SlugField(verbose_name="slug", max_length=50, null=False, blank=False, db_index=True, unique=True)
    slug.pre_save = slugify_save
    status = models.IntegerField(verbose_name="Status", choices=PRODUCT_STATUS, null=False, blank=False, default=1)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class Color(BaseMixin):
    name = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False, db_index=True, unique=True)
    slug = models.SlugField(verbose_name="slug", max_length=50, null=False, blank=False, db_index=True, unique=True)
    slug.pre_save = slugify_save

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.name


SIZE = (
    (1, 'Único'),
    (2, 'PP'),
    (3, 'P'),
    (4, 'M'),
    (5, 'G'),
    (6, 'GG')
)


class Sku(BaseMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name="skus")
    size = models.IntegerField(verbose_name="Tamanho", choices=SIZE, null=False, blank=False, default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=False, blank=False, related_name="color_skus")

    class Meta:
        verbose_name = 'Sku'
        verbose_name_plural = 'Skus'

    def __str__(self):
        return '%s %s (%s)' % (self.product, self.color, self.get_size_display())

