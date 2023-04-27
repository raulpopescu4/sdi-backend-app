# Generated by Django 4.1.7 on 2023-04-06 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('footballTeamsApp', '0003_footballplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competitionName', models.CharField(max_length=100, unique=True)),
                ('yearOfFoundation', models.SmallIntegerField()),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CompetesIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previousParticipation', models.BooleanField()),
                ('year', models.SmallIntegerField()),
                ('competition', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='footballTeamsApp.competition')),
                ('team', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='footballTeamsApp.footballteam')),
            ],
        ),
    ]
