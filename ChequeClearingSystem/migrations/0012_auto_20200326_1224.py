# Generated by Django 3.0.4 on 2020-03-26 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChequeClearingSystem', '0011_auto_20200326_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bearerbank',
            name='user',
            field=models.ForeignKey(default=django.db.models.deletion.SET_NULL, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='payeebank',
            name='user',
            field=models.ForeignKey(default=django.db.models.deletion.SET_NULL, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
