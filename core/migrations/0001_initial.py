# Generated by Django 2.2.4 on 2019-10-20 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('semester', models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer')], max_length=64)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='PromptSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ref', models.PositiveIntegerField(blank=True)),
                ('difficulty', models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Intermediate', max_length=64)),
                ('description', models.TextField(blank=True)),
                ('hint', models.TextField(blank=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Satisfaction')),
                ('complete_count', models.PositiveIntegerField(default=0, verbose_name='# Completed')),
                ('prompt_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.PromptSet')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertag', models.CharField(blank=True, max_length=64)),
                ('completed', models.ManyToManyField(to='core.Prompt')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]