from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BasePerson


class Customer(BasePerson):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        ordering = ["id"]


class Supplier(BasePerson):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="supplier")

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")
        ordering = ["id"]
