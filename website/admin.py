from block_ip.models import BlockIP
from django.contrib import admin
from django.contrib.auth.models import User, Group

from website.models import Picture, Report


class PictureAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail', 'report_count', 'title', 'datetime', 'uploader_ip', )

admin.site.register(Picture, PictureAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)

