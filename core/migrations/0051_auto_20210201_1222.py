# Generated by Django 3.1.3 on 2021-02-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20210125_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontent',
            name='home_slider_bg_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productcontent',
            name='home_slider_title',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
