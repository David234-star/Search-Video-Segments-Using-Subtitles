# Generated by Django 5.0.6 on 2024-06-21 16:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Subtitle_ExtractSearch", "0002_rename_video_file_video_file_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="video",
            old_name="uploaded_at",
            new_name="created_at",
        ),
        migrations.RemoveField(
            model_name="subtitle",
            name="text",
        ),
        migrations.AddField(
            model_name="subtitle",
            name="subtitle_text",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="video",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="video",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="video",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="video",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="subtitle",
            name="end_time",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="subtitle",
            name="start_time",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="subtitle",
            name="video",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="Subtitle_ExtractSearch.video",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]