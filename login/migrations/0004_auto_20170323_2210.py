# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_userprofile_group_of_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='group_of_work',
            field=models.ForeignKey(default=login.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to='manager.groups_of_work'),
        ),
    ]
