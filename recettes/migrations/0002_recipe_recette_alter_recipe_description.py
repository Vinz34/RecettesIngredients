# Generated by Django 4.2 on 2023-05-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recette',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]