# Generated by Django 4.1.7 on 2023-04-17 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0014_delete_propertydetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(choices=[('type1', 'Type1'), ('type2', 'Type2')], max_length=24)),
                ('rental_type', models.CharField(choices=[('sale', 'Sale'), ('rent', 'Rent'), ('vacation_rental', 'Vacation Rental')], max_length=24)),
                ('offer_text', models.TextField()),
                ('price', models.FloatField()),
                ('phone', models.IntegerField(verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('deal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='property_detail', to='deals.deal')),
            ],
        ),
    ]
