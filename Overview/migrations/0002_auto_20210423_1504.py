# Generated by Django 3.2 on 2021-04-23 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Overview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_title', models.CharField(max_length=64)),
                ('offer_detail', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product Categories'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='quantity_in_stock',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='THis is used in assigning user friendly components into the material', max_length=250),
        ),
        migrations.AddField(
            model_name='product',
            name='sold_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='name',
            field=models.CharField(default='Sports', max_length=32, unique=True),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Overview.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Overview.product'),
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
        migrations.AddField(
            model_name='dailyoffer',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Overview.product'),
        ),
    ]
