# Generated by Django 5.0.7 on 2024-07-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_customeraddress_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]
