# Generated by Django 3.1.3 on 2020-11-02 17:23

import core.models
from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20201102_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontent',
            name='features_page_metrics_2',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=core.models.get_default_list, size=None),
        ),
        migrations.AddField(
            model_name='productcontent',
            name='pricing_page_amount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcontent',
            name='pricing_page_emi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]