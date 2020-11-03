# Generated by Django 3.1.3 on 2020-11-02 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]