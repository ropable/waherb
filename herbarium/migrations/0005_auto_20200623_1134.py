# Generated by Django 3.0.7 on 2020-06-23 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herbarium', '0004_texpressdata_row_text'),
    ]

    operations = [
        migrations.RunSQL('CREATE INDEX ON herbarium_texpressdata USING GIN (row_text gin_trgm_ops);'),
    ]
