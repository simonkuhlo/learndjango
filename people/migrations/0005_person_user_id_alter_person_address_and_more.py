# Generated by Django 4.2.7 on 2023-11-11 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0004_remove_person_contact_person_address_person_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.address'),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='discord',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='instagram',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='steam',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
