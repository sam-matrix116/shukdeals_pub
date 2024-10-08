# Generated by Django 4.1.7 on 2023-08-01 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0104_tranzilatoken'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranzilaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('plan', 'Plan'), ('deal', 'Deal')], default='plan', max_length=20)),
                ('locations_to_activate', models.IntegerField(default=0)),
                ('amount', models.FloatField(default=0.0)),
                ('currency', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plan_to_activate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.plan')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tranzila_detail', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
