# Generated by Django 5.0.6 on 2024-07-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_usermodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
