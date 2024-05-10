# Generated by Django 5.0.6 on 2024-05-09 12:30

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='KZ'),
        ),
    ]