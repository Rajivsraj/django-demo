# Generated by Django 4.1.7 on 2023-04-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='phone',
            field=models.CharField(default='', max_length=50),
        ),
    ]
