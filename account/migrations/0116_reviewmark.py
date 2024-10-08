# Generated by Django 4.1.7 on 2023-08-07 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0115_alter_tranziladetail_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark_type', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked_review', to='account.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked_by_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
