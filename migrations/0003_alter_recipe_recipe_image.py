# Generated by Django 4.2.15 on 2024-08-26 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0002_recipe_delete_receipe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="recipe_image",
            field=models.ImageField(upload_to="recipe/"),
        ),
    ]