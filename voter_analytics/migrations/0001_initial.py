# Generated by Django 5.1.1 on 2024-11-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('street_num', models.IntegerField()),
                ('street_name', models.TextField()),
                ('apartment_num', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('registration_date', models.DateField()),
                ('party_affiliation', models.CharField(max_length=1)),
                ('precinct_num', models.IntegerField()),
                ('v20state', models.BooleanField()),
                ('v21town', models.BooleanField()),
                ('v21primary', models.BooleanField()),
                ('v22general', models.BooleanField()),
                ('v23town', models.BooleanField()),
            ],
        ),
    ]
