# Generated by Django 4.2 on 2023-04-18 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('teams', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isEventAdmin', models.BooleanField(default=False)),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('teamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teams')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]