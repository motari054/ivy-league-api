# Generated by Django 5.1.3 on 2024-12-09 14:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0013_alter_blogs_content_alter_blogs_sub_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogs",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]