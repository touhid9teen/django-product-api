# Generated by Django 5.1 on 2024-08-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_with_tax',
            field=models.FloatField(null=True),
        ),
    ]
