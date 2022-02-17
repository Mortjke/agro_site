# Generated by Django 2.2.16 on 2022-02-16 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales_backend', '0002_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.AddField(
            model_name='product',
            name='product_seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_seller', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]