# Generated by Django 4.2 on 2023-05-12 11:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0006_alter_customer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storeapp.product')),
            ],
        ),
    ]