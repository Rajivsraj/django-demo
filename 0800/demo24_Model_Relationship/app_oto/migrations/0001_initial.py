# Generated by Django 4.1.7 on 2023-10-20 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMarksheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='app_oto.studentdetail')),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('english', models.IntegerField()),
                ('skt', models.IntegerField()),
                ('total', models.IntegerField()),
                ('average', models.IntegerField()),
            ],
        ),
    ]
