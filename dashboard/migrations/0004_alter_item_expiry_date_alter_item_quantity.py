# Generated by Django 4.2.14 on 2024-08-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_item_location_delete_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
