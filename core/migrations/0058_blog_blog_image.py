# Generated by Django 3.1.3 on 2021-03-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.TextField(default='file:///E:/Emotorad/emotorad/src/assets/img/backgrounds/blogpost.jpg'),
            preserve_default=False,
        ),
    ]
