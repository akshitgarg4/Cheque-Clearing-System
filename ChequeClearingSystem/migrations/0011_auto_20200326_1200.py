# Generated by Django 3.0.4 on 2020-03-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ChequeClearingSystem', '0010_auto_20200325_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='bearerbank',
            name='registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payeebank',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
