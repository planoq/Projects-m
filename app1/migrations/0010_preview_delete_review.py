# Generated by Django 5.0.2 on 2024-02-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=30)),
                ('star', models.IntegerField()),
                ('kk', models.IntegerField()),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
