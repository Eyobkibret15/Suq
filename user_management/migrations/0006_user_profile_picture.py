# Generated by Django 4.1.4 on 2022-12-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0005_alter_user_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(blank=True, upload_to="static/media"),
        ),
    ]
