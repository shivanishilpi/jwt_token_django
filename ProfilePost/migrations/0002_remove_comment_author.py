# Generated by Django 3.2.22 on 2023-10-16 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProfilePost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
