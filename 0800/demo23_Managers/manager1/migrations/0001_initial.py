# Generated by Django 4.1.7 on 2023-10-16 15:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
            ],
            managers=[
                ('myManger', django.db.models.manager.Manager()),
            ],
        ),
    ]
