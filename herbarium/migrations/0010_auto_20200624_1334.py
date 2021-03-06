# Generated by Django 3.0.7 on 2020-06-24 05:34

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('herbarium', '0009_auto_20200624_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectingevent',
            name='location_description',
        ),
        migrations.RemoveField(
            model_name='collectingevent',
            name='point',
        ),
        migrations.RemoveField(
            model_name='collectingevent',
            name='spatial_accuracy',
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('spatial_accuracy', models.CharField(blank=True, choices=[('10000 m', '10000 m'), ('1000 m', '1000 m'), ('100 m', '100 m'), ('10 m', '10 m'), ('1 m', '1 m')], max_length=64, null=True)),
                ('point', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4283)),
                ('polygon', django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4283)),
                ('altitude', models.FloatField(blank=True, help_text='Metres above/below surface level.', null=True)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('creator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='herbarium_location_created', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='herbarium_location_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='collectingevent',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='herbarium.Location'),
        ),
    ]
