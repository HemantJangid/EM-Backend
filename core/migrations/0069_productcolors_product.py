# Generated by Django 3.1.3 on 2021-04-26 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20210426_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcolors',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.product'),
            preserve_default=False,
        ),
    ]
