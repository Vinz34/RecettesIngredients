# Generated by Django 4.2 on 2023-05-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='../static/unknown.png', upload_to='uploads/'),
        ),
    ]
