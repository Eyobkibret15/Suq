# Generated by Django 4.1.4 on 2023-01-06 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0011_alter_user_email_alter_user_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]