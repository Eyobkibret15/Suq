# Generated by Django 4.1.4 on 2023-03-10 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "shopping_process",
            "0002_remove_cartitem_session_id_cartitem_user_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderdetail",
            name="payment_id",
        ),
    ]