# Generated by Django 4.0.3 on 2022-04-18 00:36

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="grade",
            name="slug",
        ),
        migrations.AddField(
            model_name="grade",
            name="created",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="grade",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sub_grade",
                to="student.grade",
            ),
        ),
    ]