# Generated by Django 3.2.6 on 2021-09-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210829_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
