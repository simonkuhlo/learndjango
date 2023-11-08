# Generated by Django 4.2.7 on 2023-11-08 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('key_manager', '0005_remove_key_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.AlterField(
            model_name='key',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.adress'),
        ),
        migrations.DeleteModel(
            name='Adress',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]