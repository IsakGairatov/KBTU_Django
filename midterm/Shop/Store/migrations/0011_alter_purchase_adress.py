# Generated by Django 5.0.3 on 2024-03-12 01:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_alter_adress_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='adress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Store.adress'),
        ),
    ]