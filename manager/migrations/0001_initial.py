# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 20:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=300)),
                ('inventory_number', models.IntegerField()),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='groups_of_reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='groups_of_work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='issue',
            fields=[
                ('number_issue', models.IntegerField(primary_key=True, serialize=False)),
                ('number_history', models.IntegerField()),
                ('brief_description', models.CharField(max_length=200)),
                ('start_downtime', models.DateTimeField()),
                ('start_issue', models.DateTimeField()),
                ('progress', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='level_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_state', models.PositiveSmallIntegerField()),
                ('description', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='status_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
                ('fio', models.CharField(max_length=200)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('id_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.State')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('change_date', models.DateTimeField(verbose_name='date changed')),
                ('user_edit', models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_coordinator', to='manager.workers', verbose_name='Координатор'),
        ),
        migrations.AddField(
            model_name='issue',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_creator', to='manager.workers', verbose_name='Инициатор'),
        ),
        migrations.AddField(
            model_name='issue',
            name='equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equipment'),
        ),
        migrations.AddField(
            model_name='issue',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_executor', to='manager.workers', verbose_name='Исполнитель'),
        ),
        migrations.AddField(
            model_name='issue',
            name='groups_of_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.groups_of_work'),
        ),
        migrations.AddField(
            model_name='issue',
            name='reason',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.solutions'),
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.status_issue'),
        ),
        migrations.AddField(
            model_name='issue',
            name='user_edit',
            field=models.ForeignKey(default=manager.models.uknown_user, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='issue',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.workspace'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.workspace'),
        ),
    ]
