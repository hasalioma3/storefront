# Generated by Django 4.1a1 on 2022-06-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_rename_price_product_unit_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(default="-"),
            preserve_default=False,
        ),
    ]
