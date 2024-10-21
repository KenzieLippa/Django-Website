# Generated by Django 5.1.1 on 2024-10-17 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_alter_profile_email_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.profile')),
                ('status_msg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mini_fb.statusmsg')),
            ],
        ),
    ]
