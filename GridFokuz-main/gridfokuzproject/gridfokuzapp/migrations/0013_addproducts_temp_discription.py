# Generated by Django 4.2 on 2023-06-16 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gridfokuzapp', '0012_addproducts_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addproducts',
            name='temp_discription',
            field=models.CharField(max_length=250, null=True),
        ),
    ]