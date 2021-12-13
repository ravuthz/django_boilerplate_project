# Generated by Django 3.1.6 on 2021-11-25 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='is_removed', when={True})),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='code', unique=True)),
                ('code', models.SlugField(max_length=255)),
                ('desc', models.TextField(max_length=255, null=True)),
                ('payment_type', models.CharField(choices=[('CASH', 'Cash'), ('CREDIT', 'Credit'), ('CHEQUE', 'Cheque')], default='CASH', max_length=255)),
                ('payment_status', models.CharField(choices=[('FULL', 'Full'), ('ADVANCE', 'Advance'), ('NO_PAYMENT', 'No Payment')], default='FULL', max_length=255)),
                ('customer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'pos_order',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_removed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='is_removed', when={True})),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Order Item',
                'verbose_name_plural': 'Orders Items',
                'db_table': 'pos_order_item',
                'ordering': ['id'],
            },
        ),
    ]