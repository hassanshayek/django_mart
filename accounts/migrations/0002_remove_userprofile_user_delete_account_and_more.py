# Generated by Django 4.2.3 on 2023-10-06 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_product_product_name_delete_reviewrating"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.DeleteModel(
            name="Account",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
