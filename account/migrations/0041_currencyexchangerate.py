# Generated by Django 4.1.7 on 2023-04-12 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0040_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_date', models.DateField()),
                ('exchange_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('from_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frm_cur', to='account.currency')),
                ('to_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_cur', to='account.currency')),
            ],
            options={
                'unique_together': {('from_currency', 'to_currency', 'rate_date')},
            },
        ),
    ]
