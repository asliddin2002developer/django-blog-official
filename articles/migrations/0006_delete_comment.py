# Generated by Django 4.0.5 on 2022-06-17 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_comment_comment_body'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
