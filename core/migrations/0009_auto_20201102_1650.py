# Generated by Django 3.1.3 on 2020-11-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_productcontent_landing_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontent',
            name='landing_page_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
