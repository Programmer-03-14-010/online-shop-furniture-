from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from products.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "PENDING"
        ACCEPTED = "ACCEPTED"
        DELIVERING = "DELIVERING"
        DELIVERED = "DELIVERED"
        CANCELED = "CANCELED"

    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name="orders")

    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r"^\+998[0-9]{9}$",
                message="Telefon raqami +998XXXXXXXXX formatida bo‘lishi kerak."
            )
        ]
    )

    email = models.EmailField()

    full_name = models.CharField(max_length=128)

    address = models.CharField(max_length=255)

    total_products = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    status = models.CharField(choices=OrderStatus, default=OrderStatus.PENDING, max_length=128)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")

    product = models.ForeignKey(
        ProductModel, on_delete=models.SET_NULL,
        related_name="orders", null=True, blank=True
    )

    product_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    product_title = models.CharField(max_length=255)

    product_quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.product.title if self.product else "Unknown product"

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = "order item"
        verbose_name_plural = "order items"
