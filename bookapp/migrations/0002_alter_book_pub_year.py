# Generated by Django 4.2.2 on 2023-06-09 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="pub_year",
            field=models.IntegerField(
                default=datetime.datetime(
                    2023, 6, 9, 3, 40, 7, 807300, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
