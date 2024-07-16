# Generated by Django 5.0.6 on 2024-07-15 20:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valuesconsumedperday',
            name='id_nutrition_personal_details',
        ),
        migrations.CreateModel(
            name='ValuesRecommendedPerDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('cals', models.FloatField()),
                ('water', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_nutrition_personal_details', models.ForeignKey(db_column='id_nutrition_personal_details', null=True, on_delete=django.db.models.deletion.CASCADE, to='nutrition.nutritionpersonaldetails')),
            ],
            options={
                'db_table': 'values_recommended_per_day',
            },
        ),
        migrations.AddField(
            model_name='valuesconsumedperday',
            name='id_recommended_values',
            field=models.ForeignKey(db_column='id_recommended_values', null=True, on_delete=django.db.models.deletion.CASCADE, to='nutrition.valuesrecommendedperday'),
        ),
    ]
