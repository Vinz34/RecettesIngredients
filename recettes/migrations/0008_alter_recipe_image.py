# Generated by Django 4.2 on 2023-05-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0007_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='uploads/unknown.jpg', upload_to='uploads/'),
        ),
    ]
