# Generated by Django 4.1 on 2022-09-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skill", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="description",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="description"
            ),
        ),
    ]
