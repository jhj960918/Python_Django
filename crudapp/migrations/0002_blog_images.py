# Generated by Django 3.0.8 on 2020-07-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
