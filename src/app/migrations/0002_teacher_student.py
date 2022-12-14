# Generated by Django 4.0.6 on 2022-08-02 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='teacher/profile')),
                ('teacher_id', models.CharField(blank=True, max_length=10, unique=True)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('class_taught', models.CharField(blank=True, max_length=255)),
                ('contact_number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(upload_to='student/profile')),
                ('registration_id', models.CharField(blank=True, max_length=10, unique=True)),
                ('standard', models.CharField(blank=True, max_length=10)),
                ('class_section', models.CharField(blank=True, max_length=10)),
                ('stream', models.CharField(blank=True, max_length=50)),
                ('roll_number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
