# Generated by Django 5.0.6 on 2024-05-16 19:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_like_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
