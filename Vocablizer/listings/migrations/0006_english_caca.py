# Generated by Django 4.1 on 2024-07-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_remove_english_example_example'),
    ]

    operations = [
        migrations.AddField(
            model_name='english',
            name='caca',
            field=models.BooleanField(default=False),
        ),
    ]