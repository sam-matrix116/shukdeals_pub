# Generated by Django 4.1.7 on 2023-04-18 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reviewers', to=settings.AUTH_USER_MODEL),
        ),
    ]
