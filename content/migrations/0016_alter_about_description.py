# Generated by Django 4.1.7 on 2024-06-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_alter_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
