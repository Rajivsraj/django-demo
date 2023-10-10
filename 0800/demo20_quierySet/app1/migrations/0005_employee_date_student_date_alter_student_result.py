# Generated by Django 4.2.2 on 2023-10-03 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_students_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='result',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Fail', 'Fail')], max_length=50),
        ),
    ]