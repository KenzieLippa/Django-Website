# Generated by Django 5.1.1 on 2024-12-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OregonTrail_V2', '0012_game_miles'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='currentInjury',
            field=models.TextField(default='IJ.NONE'),
        ),
        migrations.AddField(
            model_name='character',
            name='dead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='character',
            name='deathChance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='healthLoss',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='infected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='character',
            name='restDaysNeeded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='slowHeal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='stomach',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='character',
            name='treated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='days',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='playersAlive',
            field=models.IntegerField(default=5),
        ),
    ]
