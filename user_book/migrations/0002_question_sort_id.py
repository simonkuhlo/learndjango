# Generated by Django 4.2.7 on 2023-11-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sort_id',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
