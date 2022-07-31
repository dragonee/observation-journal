# Generated by Django 3.2.12 on 2022-07-31 04:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('description', models.TextField(help_text='Describe the reward')),
            ],
        ),
        migrations.CreateModel(
            name='RewardTableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(default=1)),
                ('calculate_each', models.BooleanField(default=True, verbose_name='Each')),
                ('fail_percent', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='%0')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rewards.reward')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table', to='rewards.reward')),
            ],
        ),
    ]
