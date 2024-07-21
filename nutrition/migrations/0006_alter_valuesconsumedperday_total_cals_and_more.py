# Generated by Django 5.0.6 on 2024-07-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0005_alter_valuesconsumedperday_total_cals_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuesconsumedperday',
            name='total_cals',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='valuesconsumedperday',
            name='total_carbs',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='valuesconsumedperday',
            name='total_fat',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='valuesconsumedperday',
            name='total_protein',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='valuesconsumedperday',
            name='total_water',
            field=models.FloatField(default=0, null=True),
        ),
    ]
