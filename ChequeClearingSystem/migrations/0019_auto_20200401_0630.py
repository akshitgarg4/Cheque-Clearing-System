# Generated by Django 3.0.4 on 2020-04-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ChequeClearingSystem', '0018_auto_20200401_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bearerbank',
            name='lastTransaction',
            field=models.DateField(null=True, verbose_name='Last Transaction'),
        ),
        migrations.AlterField(
            model_name='payeebank',
            name='lastTransaction',
            field=models.DateField(null=True, verbose_name='Last Transaction'),
        ),
    ]
