# Generated by Django 3.2 on 2021-04-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0002_auto_20210423_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.ImageField(blank=True, upload_to='products/images/cover'),
        ),
    ]