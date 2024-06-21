from django.db import models
import uuid


class Video(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    title = models.CharField(null=True, blank=True, max_length=255)
    file = models.FileField(upload_to="uploads/")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.uuid} -- {self.title}"


class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=20, null=True)
    end_time = models.CharField(max_length=20, null=True)
    subtitle_text = models.TextField(null=True)

    def __str__(self) -> str:
        return f"{self.video} -- {self.end_time}"
