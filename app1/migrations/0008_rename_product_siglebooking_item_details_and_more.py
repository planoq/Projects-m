# Generated by Django 5.0.2 on 2024-02-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_siglebooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siglebooking',
            old_name='product',
            new_name='item_details',
        ),
        migrations.RenameField(
            model_name='siglebooking',
            old_name='user',
            new_name='user_details',
        ),
        migrations.AddField(
            model_name='siglebooking',
            name='date',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siglebooking',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='siglebooking',
            name='tprice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siglebooking',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='siglebooking',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
