from django.contrib import admin
from embed_video.admin import AdminVideoMixin

# Register your models here.

from .models import EmbedVideo

class EmbedVideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(EmbedVideo, EmbedVideoAdmin)