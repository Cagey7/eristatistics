# Generated by Django 4.2.6 on 2023-11-23 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True, verbose_name='Название разделала')),
                ('slug', models.CharField(max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EconomicIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=127, unique=True)),
                ('macro_topic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='macrobulletin.topic')),
            ],
        ),
    ]
