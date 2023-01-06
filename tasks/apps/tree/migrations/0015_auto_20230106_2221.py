# Generated by Django 3.2.16 on 2023-01-06 22:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0014_thread_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='id',
        ),
        migrations.AlterField(
            model_name='thread',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
