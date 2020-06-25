# Generated by Django 3.0.4 on 2020-06-24 08:45

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mappage',
            name='formatted_address',
        ),
        migrations.RemoveField(
            model_name='mappage',
            name='latlng_address',
        ),
        migrations.AddField(
            model_name='mappage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]