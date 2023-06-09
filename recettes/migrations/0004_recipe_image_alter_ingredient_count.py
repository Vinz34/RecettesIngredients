# Generated by Django 4.2 on 2023-05-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0003_ingredient_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='', upload_to='recettes/'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
