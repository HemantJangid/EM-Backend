# Generated by Django 3.1.3 on 2020-11-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_productcontent_features_page_heading_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model_number',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]