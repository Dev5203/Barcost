# Generated by Django 4.1.6 on 2023-02-10 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0006_pricehistory_remove_product_price_history_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricehistory',
            options={'get_latest_by': 'date'},
        ),
    ]
