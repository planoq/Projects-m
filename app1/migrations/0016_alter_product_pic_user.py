# Generated by Django 5.0.2 on 2024-03-04 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_product_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_pic',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.products'),
        ),
    ]