# Generated by Django 5.0.3 on 2024-03-09 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0005_alter_userinfo_default_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='default_adress',
        ),
    ]