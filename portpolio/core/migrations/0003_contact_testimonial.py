# Generated by Django 4.1.4 on 2023-05-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_skills_skill_alter_skill_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Customer Name')),
                ('email', models.EmailField(max_length=70, verbose_name='Customer email')),
                ('subject', models.CharField(max_length=70, verbose_name='Subject')),
                ('meesage', models.TextField(max_length=500, verbose_name='meesage')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name ')),
                ('profile', models.CharField(max_length=50, verbose_name='profile ')),
                ('desc', models.TextField(max_length=500, verbose_name='Description ')),
                ('image', models.ImageField(upload_to='testimonial', verbose_name='Image ')),
            ],
            options={
                'db_table': 'testimonial',
            },
        ),
    ]
