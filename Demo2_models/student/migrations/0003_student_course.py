# Generated by Django 4.1.7 on 2023-03-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[('CB', 'Computer Basic'), ('SW', 'Software'), ('HW', 'Hardware Course'), ('MM', 'Graphic Design'), ('WD', 'Web Design & Development')], default='CB', max_length=2),
        ),
    ]
