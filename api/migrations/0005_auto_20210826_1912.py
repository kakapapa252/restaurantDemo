# Generated by Django 3.2.6 on 2021-08-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210826_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppinglink',
            name='product',
        ),
        migrations.RemoveField(
            model_name='toppinglink',
            name='topping',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='toppings',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.DeleteModel(
            name='ToppingLink',
        ),
    ]
