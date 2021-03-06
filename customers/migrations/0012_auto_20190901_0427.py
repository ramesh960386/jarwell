# Generated by Django 2.2.3 on 2019-09-01 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20190901_0403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_qty',
        ),
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_qty', models.IntegerField(default=0)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('payment_status', models.IntegerField(default=0)),
                ('shipping_status', models.BooleanField(default=False)),
                ('notes', models.TextField(default='None')),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.Order')),
            ],
        ),
    ]
