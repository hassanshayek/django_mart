# Generated by Django 4.2.3 on 2023-10-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_alter_product_product_name_reviewrating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name="ReviewRating",
        ),
    ]