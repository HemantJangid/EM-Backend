# Generated by Django 3.1.3 on 2021-05-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_communityuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityuser',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
