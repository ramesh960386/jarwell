# Generated by Django 2.2.3 on 2019-08-31 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_item_date_encoded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='total_price',
        ),
    ]
