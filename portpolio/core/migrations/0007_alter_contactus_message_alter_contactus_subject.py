# Generated by Django 4.1.4 on 2023-05-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.TextField(max_length=55),
        ),
    ]
