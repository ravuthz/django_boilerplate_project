from django.contrib import admin

from apps.users.models import Customer, Supplier
from core.admins import CoreModelAdmin
from core.constants import date_fields


@admin.register(Customer)
class CustomerModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'user',
                       'phone',
                   ) + date_fields

    list_filter = (
                      'user',
                      'is_removed',
                  ) + date_fields

    date_hierarchy = 'created_at'


@admin.register(Supplier)
class SupplierModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'user',
                       'phone',
                   ) + date_fields

    list_filter = (
                      'user',
                      'is_removed',
                  ) + date_fields

    date_hierarchy = 'created_at'
