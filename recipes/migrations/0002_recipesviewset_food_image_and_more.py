# Generated by Django 5.0.6 on 2024-07-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesviewset',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/recipes/'),
        ),
        migrations.AddField(
            model_name='recipesviewset',
            name='recomendation',
            field=models.TextField(blank=True),
        ),
    ]
