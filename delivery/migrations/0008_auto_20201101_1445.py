# Generated by Django 3.1.2 on 2020-11-01 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20201101_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_product',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='delivery.product'),
        ),
    ]
