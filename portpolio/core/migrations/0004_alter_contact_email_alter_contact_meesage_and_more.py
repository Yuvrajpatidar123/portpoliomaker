# Generated by Django 4.1.4 on 2023-05-25 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='meesage',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=70),
        ),
    ]
