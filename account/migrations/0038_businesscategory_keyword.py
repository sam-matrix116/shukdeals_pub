# Generated by Django 4.1.7 on 2023-04-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0037_remove_businesscategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscategory',
            name='keyword',
            field=models.CharField(max_length=50, null=True, verbose_name='Category Keyword'),
        ),
    ]
