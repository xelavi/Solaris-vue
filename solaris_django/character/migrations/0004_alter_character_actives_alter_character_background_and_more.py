# Generated by Django 5.1.3 on 2024-12-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_alter_character_background_alter_character_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='actives',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='backgroundskills',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='job',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='jobskills',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='jobtalents',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='martialStyle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='martialStyletalents',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='skillsadded',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
