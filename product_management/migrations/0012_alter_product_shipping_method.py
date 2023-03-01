# Generated by Django 4.1.4 on 2023-02-27 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product_management", "0011_product_shipping_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="shipping_method",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="product_management.shippingmethod",
            ),
        ),
    ]
