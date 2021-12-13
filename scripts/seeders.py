from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django_extensions.management.base import logger
from django_seed import Seed
from phonenumbers.util import force_unicode

from apps.products.models import Category, Product


# python manage.py runscript seeders

def run():
    seeder = Seed.seeder()
    logger.info("Start seeding apps.products.Category")
    category, is_created_category = Category.objects.get_or_create(
        name="Cate 1",
        defaults={
            "slug": "cate_1",
            "desc": "Category 1"
        })

    seeder.add_entity(Category, 1)
    saved_category = seeder.execute()
    print(saved_category)

    logger.info("Start seeding apps.products.Product")
    seeder.add_entity(Product, 10, {
        'category': category
    })
    saved_products = seeder.execute()
    print(saved_products)

    LogEntry.objects.log_action(
        user_id=1,
        content_type_id=ContentType.objects.get_for_model(category).pk,
        object_id=category.pk,
        object_repr=force_unicode(category),
        action_flag=ADDITION,
    )
