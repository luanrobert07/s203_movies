# Generated by Django 3.0.6 on 2024-03-22 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0013_auto_20200611_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
