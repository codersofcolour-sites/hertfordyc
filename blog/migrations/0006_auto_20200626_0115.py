# Generated by Django 3.0.4 on 2020-06-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpage_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
