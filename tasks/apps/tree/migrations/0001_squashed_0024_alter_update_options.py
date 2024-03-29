# Generated by Django 3.2.16 on 2023-01-08 23:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('tree', '0001_initial'), ('tree', '0002_auto_20191030_1847'), ('tree', '0003_auto_20191030_1850'), ('tree', '0004_board_focus'), ('tree', '0005_auto_20191227_1548'), ('tree', '0006_plan_reflection'), ('tree', '0007_auto_20200111_2143'), ('tree', '0008_observation_observationtype'), ('tree', '0009_auto_20200302_2229'), ('tree', '0010_observation_date_closed'), ('tree', '0011_update'), ('tree', '0012_alter_board_state'), ('tree', '0013_auto_20230106_2204'), ('tree', '0014_thread_uuid'), ('tree', '0015_auto_20230106_2221'), ('tree', '0016_rename_uuid_thread_id'), ('tree', '0017_remove_observation_thread'), ('tree', '0018_observation_thread'), ('tree', '0019_observation_uuid'), ('tree', '0020_auto_20230108_1759'), ('tree', '0021_rename_uuid_observation_id'), ('tree', '0022_remove_update_observation'), ('tree', '0023_update_observation'), ('tree', '0024_alter_update_options')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ObservationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('pub_date', models.DateField()),
                ('situation', models.TextField(blank=True, help_text='What happened?', null=True)),
                ('interpretation', models.TextField(blank=True, help_text='How you saw it, what you felt?', null=True)),
                ('approach', models.TextField(blank=True, help_text='How should you approach it in the future?', null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.observationtype')),
                ('date_closed', models.DateField(blank=True, help_text='Closed', null=True)),
                ('thread', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tree.thread')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(help_text='Update')),
                ('observation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tree.observation')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
