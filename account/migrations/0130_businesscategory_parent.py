# Generated by Django 4.1.7 on 2023-08-23 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0129_delete_businesssubcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscategory',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.businesscategory'),
        ),
    ]
