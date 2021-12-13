from django.contrib import admin

from apps.settings.models import Setting, SettingItem
from core.admins import CoreModelAdmin, CoreTabularInlineAdmin
from core.constants import date_fields


class SettingItemAdminInline(CoreTabularInlineAdmin):
    model = SettingItem
    fields = (
        'slug',
        'name',
        'desc',
        'value',
    )
    list_display = (
                       'id',
                       'setting',
                       'slug',
                       'name',
                       'desc',
                       'value',
                   ) + date_fields


@admin.register(Setting)
class SettingModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'slug',
                       'name',
                       'desc',
                   ) + date_fields

    list_filter = (
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug', 'name')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
    inlines = (SettingItemAdminInline,)


@admin.register(SettingItem)
class SettingItemModelAdmin(CoreModelAdmin):
    list_display = (
                       'id',
                       'setting',
                       'slug',
                       'name',
                       'desc',
                       'value',
                   ) + date_fields

    list_filter = (
                      'setting',
                      'is_removed',
                  ) + date_fields

    search_fields = ('slug', 'name')
    prepopulated_fields = {'slug': ['name']}
    date_hierarchy = 'created_at'
