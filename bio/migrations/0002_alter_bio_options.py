# Generated by Django 4.2.17 on 2024-12-18 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bio',
            options={'ordering': ['-name']},
        ),
    ]
