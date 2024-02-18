# Generated by Django 4.1.6 on 2023-02-08 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0002_product_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='price_history',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PriceHistoryProduct', to='Tracker.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
