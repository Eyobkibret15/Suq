# Generated by Django 4.1.4 on 2023-03-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping_process", "0004_alter_orderdetail_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetail",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
