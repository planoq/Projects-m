# Generated by Django 5.0.2 on 2024-02-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_preview_delete_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('messge', models.CharField(max_length=200)),
            ],
        ),
    ]
