# Generated by Django 5.1.3 on 2024-12-04 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_rename_offer_end_date_product_discount_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="discount",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
