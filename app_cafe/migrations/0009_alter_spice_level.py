# Generated by Django 5.0.3 on 2024-03-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cafe", "0008_remove_hotdog_spices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spice",
            name="level",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
