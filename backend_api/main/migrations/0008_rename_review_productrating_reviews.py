# Generated by Django 5.0.7 on 2024-07-20 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_productrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productrating',
            old_name='review',
            new_name='reviews',
        ),
    ]
