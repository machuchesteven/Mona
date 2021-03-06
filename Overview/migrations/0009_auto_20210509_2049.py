# Generated by Django 3.2 on 2021-05-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0008_auto_20210509_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Overview.productcategory'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default='Uncategorized', max_length=32, unique=True),
        ),
    ]
