# Generated by Django 4.2.5 on 2023-10-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_student1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studetn2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60, null=True)),
                ('city2', models.CharField(blank=True, max_length=50)),
                ('city3', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
