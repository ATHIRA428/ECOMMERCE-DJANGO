# Generated by Django 4.2.2 on 2023-06-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
