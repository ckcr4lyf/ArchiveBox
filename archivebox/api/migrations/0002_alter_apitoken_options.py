# Generated by Django 5.0.4 on 2024-04-26 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apitoken',
            options={'verbose_name': 'API Key', 'verbose_name_plural': 'API Keys'},
        ),
    ]