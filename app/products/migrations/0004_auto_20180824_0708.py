# Generated by Django 2.1 on 2018-08-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180824_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoptionprice',
            name='price',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=12, verbose_name='가격'),
        ),
    ]
