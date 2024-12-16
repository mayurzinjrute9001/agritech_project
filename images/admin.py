from django.contrib import admin
from .models.UploadedImage import UploadedImage


# Register your models here.
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at', 'extracted_text')


admin.site.register(UploadedImage,UploadedImageAdmin)
