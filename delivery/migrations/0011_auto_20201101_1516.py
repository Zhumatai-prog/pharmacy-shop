# Generated by Django 3.1.2 on 2020-11-01 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_auto_20201101_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_supply',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.product'),
        ),
        migrations.AlterField(
            model_name='product_sale',
            name='product',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.product'),
        ),
        migrations.AlterField(
            model_name='product_supply',
            name='order',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.order_product'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='personnel',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='delivery.personnel'),
        ),
    ]