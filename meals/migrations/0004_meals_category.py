# Generated by Django 3.2.8 on 2021-10-18 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='meals',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='meals.category'),
        ),
    ]
