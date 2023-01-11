# Generated by Django 3.2.16 on 2023-01-08 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_squashed_0024_alter_update_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.thread'),
        ),
        migrations.AlterField(
            model_name='update',
            name='observation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.observation'),
        ),
    ]