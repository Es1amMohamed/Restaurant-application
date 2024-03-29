# Generated by Django 5.0.1 on 2024-02-07 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0005_alter_items_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="category",
                to="items.category",
            ),
        ),
    ]
