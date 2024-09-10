# Generated by Django 4.1.7 on 2023-06-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0082_remove_stripedetail_client_secret_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planfeature',
            name='feature_type',
            field=models.CharField(choices=[('deal', 'Deal'), ('classified', 'Classified'), ('news', 'News'), ('job', 'Job')], default='deal', max_length=20),
        ),
    ]
