# Generated by Django 3.2.8 on 2021-10-18 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_meals_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
