from django.shortcuts import render, redirect, HttpResponse
from .forms import VideoForm
from .tasks import process_video
from .models import Video
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import boto3


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'list.html', {'videos': videos})


def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.is_active = False
            video.save()
            video_file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(f'uploads/video_{video.uuid}.mp4', video_file)
            messages.info(request, "The video is processing")
            process_video.delay(video.uuid)
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload.html', {'form': form})


def search_videos(request, video_id):
    keyword = request.GET.get('keyword')
    video_file = Video.objects.filter(uuid=video_id).first()
    if not video_file.is_active:
        return HttpResponse("Video is been processing")
    results = []
    context = {"title": video_file.title}

    if keyword:
        dynamodb = boto3.client('dynamodb', region_name='us-east-1')
        table_name = 'nosqlsubtitle_db'
        filter_expression = 'VideoId = :video'
        expression_attribute_values = {
            ':video': {'S': video_id},
        }
        response = dynamodb.scan(
            TableName=table_name,
            FilterExpression=filter_expression,
            ExpressionAttributeValues=expression_attribute_values
        )
        results = response.get('Items', [])
        matching_subtitles = [item for item in results if keyword_in_subtitle(
            item['Subtitle']['S'], keyword)]
        context = {'results': matching_subtitles, 'keyword': keyword,
                   'url': video_file.file.url, "title": video_file.title}
    return render(request, 'searchthesubs.html', context)


def keyword_in_subtitle(subtitle, keyword):
    return keyword.lower() in subtitle.lower()
