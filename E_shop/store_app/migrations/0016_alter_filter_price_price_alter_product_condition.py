# Generated by Django 5.0 on 2023-12-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0015_remove_product_brand_remove_product_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('0 TO 200', '0 TO 200'), ('200 TO 400', '200 TO 400'), ('400 TO 600', '400 TO 600'), ('600 TO 800', '600 TO 800'), ('800 TO 1000', '800 TO 1000'), ('1000 TO 10000', '1000 TO 10000')], max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('GPA Certified', 'GPA Certified'), ('No', 'No')], max_length=100),
        ),
    ]
