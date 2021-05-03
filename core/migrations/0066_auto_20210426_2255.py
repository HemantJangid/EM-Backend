# Generated by Django 3.1.3 on 2021-04-26 17:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_promocode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'productImages',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
    ]