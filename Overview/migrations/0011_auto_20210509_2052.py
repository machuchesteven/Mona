# Generated by Django 3.2 on 2021-05-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0010_alter_productcategory_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default='Uncategorized', max_length=32, unique=True),
        ),
    ]
