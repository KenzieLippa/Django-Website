# Generated by Django 5.1.1 on 2024-12-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OregonTrail_V2', '0009_rename_currseasonmanager_game_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='currentGame',
        ),
        migrations.AlterField(
            model_name='game',
            name='season',
            field=models.CharField(choices=[('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall'), ('WINTER', 'Winter')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
