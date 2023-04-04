# Generated by Django 4.1.7 on 2023-03-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, db_column='fname', max_length=50, null=True)),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('dept', models.CharField(blank=True, max_length=50, null=True)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
