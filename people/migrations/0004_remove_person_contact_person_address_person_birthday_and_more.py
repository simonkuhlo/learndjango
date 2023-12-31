# Generated by Django 4.2.7 on 2023-11-09 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_contact_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='contact',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.address'),
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='discord',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='instagram',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='steam',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='twitter',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
