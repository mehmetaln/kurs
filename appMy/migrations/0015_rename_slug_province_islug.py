# Generated by Django 4.2.7 on 2024-01-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0014_province_slug_alter_kurs_province_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='province',
            old_name='slug',
            new_name='islug',
        ),
    ]
