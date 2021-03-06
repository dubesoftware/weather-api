# Generated by Django 3.0.2 on 2020-01-26 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('request_id', models.IntegerField()),
                ('request_location', models.CharField(max_length=50)),
                ('type_icon', models.CharField(max_length=50, verbose_name='type')),
                ('description', models.CharField(max_length=100)),
                ('temperature', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_bearing', models.FloatField()),
                ('wind_gust', models.FloatField()),
                ('rain_prob', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
