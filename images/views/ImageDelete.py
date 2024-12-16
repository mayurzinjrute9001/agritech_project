from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from images.models.UploadedImage import UploadedImage

class ImageDeleteView(View):
    def post(self, request, image_id):
        """Delete an image by ID."""
        image = get_object_or_404(UploadedImage, id=image_id)
        image.delete()
        return JsonResponse({"success": True})
