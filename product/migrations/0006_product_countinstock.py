# Generated by Django 3.2.16 on 2023-02-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20230211_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]