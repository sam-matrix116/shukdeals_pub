# Generated by Django 4.1.7 on 2023-08-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_remove_aboutjourney_about_remove_aboutteam_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='team_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='team_heading',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
