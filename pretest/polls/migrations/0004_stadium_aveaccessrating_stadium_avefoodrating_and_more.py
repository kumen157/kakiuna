# Generated by Django 4.1.7 on 2023-02-25 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_remove_stadium_aveaccessrating_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="stadium",
            name="aveaccessrating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="stadium",
            name="avefoodrating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="stadium",
            name="avepassionrating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="stadium",
            name="avetotalrating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="stadium",
            name="avevisibilityrating",
            field=models.FloatField(default=0),
        ),
    ]
