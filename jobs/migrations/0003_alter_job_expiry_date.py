# Generated by Django 4.1.7 on 2023-05-22 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]
