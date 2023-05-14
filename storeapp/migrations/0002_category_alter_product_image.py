# Generated by Django 4.2 on 2023-05-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
    ]
