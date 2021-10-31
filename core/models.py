from django.db import models
from django_extensions.db.fields import AutoSlugField
from model_utils.fields import MonitorField
from model_utils.models import SoftDeletableModel


class BaseModel(SoftDeletableModel, models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # deleted_at = models.DateTimeField(auto_now=False, blank=True, null=True)
    deleted_at = MonitorField(monitor='is_removed', when=[True])

    class Meta:
        abstract = True


class BaseCodeDesc(models.Model):
    slug = AutoSlugField(populate_from='code', editable=True, unique=True)
    code = models.SlugField(max_length=100, null=False, unique=False)
    desc = models.TextField(max_length=255, null=True)
    # desc_en = models.TextField(max_length=255, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.desc

    def __unicode__(self):  
        return self.desc


class BaseSlugName(models.Model):
    slug = AutoSlugField(populate_from='name', editable=True, unique=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    # name_en = models.CharField(max_length=255, null=False, unique=True)
    desc = models.TextField(max_length=255, null=True)
    # desc_en = models.TextField(max_length=255, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name