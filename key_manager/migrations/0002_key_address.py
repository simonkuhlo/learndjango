# Generated by Django 4.2.7 on 2023-11-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='address',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
