# Generated by Django 5.0.3 on 2024-03-23 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_cafe", "0013_hotdog_composition"),
    ]

    operations = [
        migrations.RenameModel(old_name="Spice", new_name="Spicy",),
        migrations.RenameField(
            model_name="hotdog_spice", old_name="spice", new_name="spicy",
        ),
    ]
