# Generated by Django 3.2.20 on 2023-08-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bills', '0002_auto_20230813_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculatedbills',
            name='bill_total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
