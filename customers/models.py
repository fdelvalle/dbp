from django.contrib.auth.models import User
from django.db import models

from dbp.models import BaseMixin


class Customer(BaseMixin):
    first_name = models.CharField(verbose_name="Nome", max_length=30, null=False, blank=False, db_index=True, unique=True)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=50, null=False, blank=False, db_index=True, unique=True)
    email = models.CharField(verbose_name="e-mail", max_length=30, null=False, blank=False, db_index=True, unique=True)
    document = models.CharField(verbose_name="CPF", max_length=11, null=False, blank=False, db_index=True, unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="Customers")

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.full_name
