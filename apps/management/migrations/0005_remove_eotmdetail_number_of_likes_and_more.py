# Generated by Django 4.2.5 on 2023-10-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0004_rename_commentor_id_eotmdetail_commentor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eotmdetail",
            name="number_of_likes",
        ),
        migrations.AddField(
            model_name="employee",
            name="number_of_likes",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="eotmdetail",
            name="commentor",
            field=models.TextField(max_length=255),
        ),
    ]