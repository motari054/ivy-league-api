# Generated by Django 5.1.3 on 2024-12-09 13:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_blogs_author_blogs_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="content",
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name="blogs",
            name="sub_title",
            field=models.CharField(max_length=300),
        ),
    ]