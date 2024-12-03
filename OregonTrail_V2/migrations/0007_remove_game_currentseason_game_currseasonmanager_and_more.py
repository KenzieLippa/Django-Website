# Generated by Django 5.1.1 on 2024-11-22 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OregonTrail_V2', '0006_alter_game_currentseason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='currentSeason',
        ),
        migrations.AddField(
            model_name='game',
            name='currSeasonManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OregonTrail_V2.season'),
        ),
        migrations.AddField(
            model_name='season',
            name='currentSeason',
            field=models.CharField(choices=[('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall'), ('WINTER', 'Winter')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='season',
            name='name',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]