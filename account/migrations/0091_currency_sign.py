# Generated by Django 4.1.7 on 2023-07-12 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0090_alter_familymember_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='sign',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
