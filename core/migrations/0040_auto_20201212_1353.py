# Generated by Django 3.1.3 on 2020-12-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_lead_form_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bg_image',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
