# Generated by Django 3.2.8 on 2021-12-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0019_product_extra_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/products/'),
        ),
    ]
