from django.db import models


class BaseMixinQuerySet(models.QuerySet):
    def only_active(self):
        return self.filter(is_active=True)


class BaseMixin(models.Model):

    objects = BaseMixinQuerySet.as_manager()

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Ativo?', db_index=True)

    def _get_label(self, field):
        return self._meta.get_field(field).verbose_name

    def _get_help_text(self, field):
        return self._meta.get_field(field).help_text

    class Meta:
        abstract = True