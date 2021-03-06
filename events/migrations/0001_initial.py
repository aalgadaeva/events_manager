# Generated by Django 3.0.6 on 2020-05-31 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', tinymce.models.HTMLField(verbose_name='Details')),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('time', models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')),
                ('num_of_attendees', models.PositiveIntegerField(blank=True, default=0)),
                ('attendees', models.ManyToManyField(blank=True, related_name='attending', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='groups.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
                'ordering': ['date', 'time'],
            },
        ),
    ]
