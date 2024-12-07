# Generated by Django 5.1.3 on 2024-12-04 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_product_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(90),
                ],
            ),
        ),
    ]
