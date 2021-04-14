from django.shortcuts import render

from django.views.generic import View
from .models import EmbedVideo

# Create your views here.
class homepage_view(View):
    def get(self, request):
        print("Homepage_get")
        return render(request, 'index.html')

    def post(self, request):
        print("Homepage_post")


def video(request):
    video = EmbedVideo.objects.all()
    return render(request, 'live.html', {'video':video})