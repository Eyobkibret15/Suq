# Generated by Django 4.1.4 on 2022-12-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0007_alter_user_profile_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="Img",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ppic",
                    models.ImageField(
                        blank=True, default="default.jpg", upload_to="profile_pics"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, default="default.jpg", upload_to="profile_pics"
            ),
        ),
    ]
