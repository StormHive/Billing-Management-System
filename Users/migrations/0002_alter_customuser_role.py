# Generated by Django 3.2.20 on 2023-08-12 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Manager', 'Manager'), ('Meter Reader', 'Meter Reader')], default=None, max_length=50, null=True),
        ),
    ]
