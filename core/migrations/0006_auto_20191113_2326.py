# Generated by Django 2.2.4 on 2019-11-14 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_accesscode_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscode',
            name='profile',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
        ),
    ]