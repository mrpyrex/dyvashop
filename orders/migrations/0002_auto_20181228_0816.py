# Generated by Django 2.1 on 2018-12-28 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='laast_name',
            new_name='last_name',
        ),
    ]
