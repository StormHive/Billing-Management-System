# Generated by Django 3.2.20 on 2023-08-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='owners_phone_number',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
