# Generated by Django 3.2.16 on 2023-01-06 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0012_alter_board_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='thread',
        ),
        migrations.RemoveField(
            model_name='reflection',
            name='thread',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
        migrations.DeleteModel(
            name='Reflection',
        ),
    ]