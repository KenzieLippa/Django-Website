# Generated by Django 5.1.1 on 2024-10-14 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0002_statusmsg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]