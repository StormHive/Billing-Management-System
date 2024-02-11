# Generated by Django 3.2.20 on 2023-08-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UnitsRate', '0002_auto_20230812_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialunitrates',
            name='commercial_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fineafterduedate',
            name='fine_after_due_date',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='miscellaneouscharges',
            name='miscellaneous_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='residentialunitrates',
            name='residential_unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]