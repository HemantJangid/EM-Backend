# Generated by Django 3.1.3 on 2020-11-02 18:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_orderitem_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
