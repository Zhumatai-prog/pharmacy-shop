# Generated by Django 3.1.2 on 2020-11-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_auto_20201101_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy_expense',
            name='month_e',
            field=models.CharField(choices=[('1-JAN', 'January'), ('2-FEB', 'February'), ('3-MAR', 'March'), ('4-APR', 'April'), ('5-MAY', 'May'), ('6-JUN', 'June'), ('7-JUL', 'July'), ('8-AUG', 'August'), ('9-SEP', 'September'), ('10-OCT', 'October'), ('11-NOV', 'November'), ('12DEC', 'December')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pharmacy_income',
            name='month_i',
            field=models.CharField(choices=[('1-JAN', 'January'), ('2-FEB', 'February'), ('3-MAR', 'March'), ('4-APR', 'April'), ('5-MAY', 'May'), ('6-JUN', 'June'), ('7-JUL', 'July'), ('8-AUG', 'August'), ('9-SEP', 'September'), ('10-OCT', 'October'), ('11-NOV', 'November'), ('12DEC', 'December')], max_length=20),
        ),
    ]
