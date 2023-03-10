from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404

from users.models import User
from .models import Video
from .services import open_file


@login_required
def get_list_video(request):
    if User.has_perm(request.user, 'video_hosting.view_video'):
        return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})
    return render(request, 'users/profile.html')


@login_required
def get_video(request, video_slug):
    _video = get_object_or_404(Video, slug=video_slug)
    return render(request, "video_hosting/video.html", {"video": _video})


@login_required
def get_streaming_video(request, video_slug):
    file, status_code, content_length, content_range = open_file(request, video_slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

