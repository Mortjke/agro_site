from django.db import models
from django.db.models.expressions import F
from django.db.models.query_utils import Q

from sales_backend.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE
    )


    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    user = models.ForeignKey(
        User,
        related_name='order_user',
        on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        User,
        related_name='seller',
        on_delete=models.CASCADE        
    )
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE        
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~Q(user=F('seller')), name='dont_buy_yourself'
            )
        ]

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
