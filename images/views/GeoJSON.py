from django.http import JsonResponse
from django.views import View
from images.models.UploadedImage import UploadedImage
import logging
logger = logging.getLogger(__name__)
class GeoJSONView(View):
    def get(self, request):
        """Serve GeoJSON data for mapping."""
        images = UploadedImage.objects.filter(latitude__isnull=False, longitude__isnull=False)
        if not images.exists():
            print("No images with geolocation found.")

        data = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [image.longitude, image.latitude],
                    },
                    "properties": {
                        "id": image.id,
                        "image_url": image.image.url,
                        "extracted_text": image.extracted_text,
                        "uploaded_at": image.uploaded_at.strftime("%Y-%m-%d %H:%M:%S"),
                    },
                }
                for image in images
            ],
        }
        return JsonResponse(data)
