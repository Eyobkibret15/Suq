# Generated by Django 4.1.4 on 2023-03-11 11:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("shopping_process", "0003_remove_orderdetail_payment_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetail",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]