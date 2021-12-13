from django.db import models
from django.utils.translation import gettext_lazy as _

from core.constants import tb_prefix
from core.models import BaseModel, BaseSlugName


class Setting(BaseModel, BaseSlugName):
    class Meta:
        db_table = tb_prefix + "setting"
        verbose_name = _("Setting")
        verbose_name_plural = _("Settings")
        ordering = ["id"]


class SettingItem(BaseModel, BaseSlugName):
    class Meta:
        db_table = tb_prefix + "setting_item"
        verbose_name = _("Setting Item")
        verbose_name_plural = _("Settings Items")
        ordering = ["id"]

    setting = models.ForeignKey(
        Setting, on_delete=models.CASCADE, default=None, null=False
    )
    value = models.TextField(
        max_length=255, null=False, blank=False
    )
