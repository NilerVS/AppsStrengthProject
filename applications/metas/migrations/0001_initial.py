# Generated by Django 4.2.6 on 2023-11-29 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, choices=[('0', 'Press banca'), ('1', 'Sentadilla'), ('2', 'Peso muerto'), ('3', 'Fondos'), ('4', 'Pull ups'), ('5', 'Chin ups')], max_length=2, null=True, verbose_name='nombre_meta')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='fecha_meta')),
                ('pr', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='PR')),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peso')),
            ],
        ),
    ]
