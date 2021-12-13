# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from django.forms import Textarea

from core.admins import CoreModelAdmin, CoreTabularInlineAdmin
from core.constants import date_fields
from .models import Category, Product, ProductVariant


class ProductVariantAdminInline(CoreTabularInlineAdmin):
    model = ProductVariant
    fields = (
        'slug',
        'code',
        'desc',
        'value',
    )
    list_display = (
                       'id',
                       'product',
                       'slug',
                       'code',
                       'desc',
                       'value',
                   ) + date_fields

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
    }


@admin.register(Category)
class CategoryModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'parent',
                       'slug',
                       'name',
                       'desc',
                   ) + date_fields

    list_filter = (
                      'parent',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug', 'name')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'


@admin.register(Product)
class ProductModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'category',
                       'slug',
                       'name',
                       'desc',
                       'price',
                       'quantity',
                   ) + date_fields

    list_filter = (
                      'category',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug', 'name')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
    inlines = (ProductVariantAdminInline,)


@admin.register(ProductVariant)
class ProductVariantModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'product',
                       'slug',
                       'code',
                       'desc',
                       'value',
                   ) + date_fields

    list_filter = (
                      'product',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug',)
    date_hierarchy = 'created_at'
