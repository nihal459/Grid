# Generated by Django 4.2 on 2023-05-09 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gridfokuzapp', '0006_rename_manualcombo_manualcombotemp'),
    ]

    operations = [
        migrations.AddField(
            model_name='manualcombotemp',
            name='usr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]