# Generated by Django 3.2.12 on 2022-07-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='description',
            field=models.TextField(blank=True, help_text='Describe the reward', null=True),
        ),
    ]
