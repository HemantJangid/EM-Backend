# Generated by Django 3.1.3 on 2021-01-06 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_dealer_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRideBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('preferred_date', models.DateField()),
                ('preferred_time', models.TimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dealer')),
            ],
            options={
                'db_table': 'test_ride_booking',
            },
        ),
    ]
