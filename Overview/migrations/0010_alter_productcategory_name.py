# Generated by Django 3.2 on 2021-05-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0009_auto_20210509_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default=1, max_length=32, unique=True),
        ),
    ]