# Generated by Django 3.1.3 on 2020-11-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontent',
            name='features_page_heading_2',
            field=models.TextField(blank=True, null=True),
        ),
    ]