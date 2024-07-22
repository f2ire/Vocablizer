# Generated by Django 4.1 on 2024-07-16 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_english_created_at_english_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='english',
            name='example',
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('example', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('english', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.english')),
            ],
        ),
    ]