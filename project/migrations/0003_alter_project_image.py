# Generated by Django 4.1 on 2022-09-14 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0002_tag_project_is_deleted_alter_project_body"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(
                blank=True,
                default="images/default.jpg",
                null=True,
                upload_to="images/",
                verbose_name="image",
            ),
        ),
    ]