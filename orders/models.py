from django.db import models

from customers.models import Customer
from dbp.models import BaseMixin
from products.models import Product

ORDER_STATUS = (
    (1, 'Novo'),
    (2, 'Aguardando Pagamento'),
    (3, 'Aprovado'),
    (4, 'Rejeitado'),
    (5, 'Cancelado')

)


class Order(BaseMixin):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="customer_orders")
    status = models.IntegerField(verbose_name="Status", choices=ORDER_STATUS, null=False, blank=False, default=1)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return '#%s (%s)' % (self.id, self.get_status_display())


class OrderItem(BaseMixin):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, null=False, blank=False, related_name="order_items")
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, null=False, blank=False, related_name="product_items")

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return '#%s (%s)' % (self.id, self.product)
