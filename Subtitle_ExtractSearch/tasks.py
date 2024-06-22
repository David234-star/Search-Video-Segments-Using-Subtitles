from celery import shared_task
import subprocess
from .models import Video
import os
from django.conf import settings
import boto3


@shared_task
def parse_time_range(time_range):
    start, end = time_range.split(' --> ')
    return start, end


@shared_task
def process_video(video_id):
    video = Video.objects.get(uuid=video_id)
    input_path = os.path.join(
        settings.MEDIA_ROOT, "uploads", f'video_{video_id}.mp4')
    output_path = os.path.join(
        settings.MEDIA_ROOT, "subtitles", f'subtitles_{video_id}.srt')
    ccextractor_command = f'D:\Downloads\ccextractor.0.85b-windows.binaries\ccextractorwinfull.exe {input_path} -o {output_path}'
    subprocess.run(ccextractor_command, shell=True)
    with open(output_path, 'r') as subtitle_file:
        subtitle_text = subtitle_file.read()
        subtitle_entries = subtitle_text.split('\n\n')
        for i in subtitle_entries:
            lines = i.split('\n')
            if len(lines) >= 3:
                sequence = lines[0]
                time_range = lines[1]
                start_time, end_time = parse_time_range(time_range)
                content = '\n'.join(lines[2:])
                content = content.strip()
                store_subtitle_in_dynamodb(
                    video_id, start_time, content, end_time)
    video.is_active = True
    video.save()
    return "done"


@shared_task
def store_subtitle_in_dynamodb(video_id, timestamp, subtitle, end_time):
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    table_name = 'nosqlsubtitle_db'
    item = {
        'VideoId': {'S': str(video_id)},
        'Timestamp': {'S': timestamp},
        'Subtitle': {'S': subtitle},
        'EndTime': {'S': end_time},
    }
    dynamodb.put_item(TableName=table_name, Item=item)
