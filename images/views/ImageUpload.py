from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from images.models.UploadedImage import UploadedImage
from PIL import Image
from images.utils.get_geolocation import get_geolocation  # Import the utility function for geolocation
import pytesseract

# Set the path for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows path

class ImageUploadView(View):

    def get(self, request):
        """Display the upload form."""
        return render(request, 'upload_image.html')

    def post(self, request):
        """Process the uploaded image and save data to the database."""
        uploaded_file = request.FILES.get('image')

        if not uploaded_file:
            return render(request, 'upload_image.html', {'error': 'Please upload an image.'})

        if not uploaded_file.content_type.startswith('image/'):
            return render(request, 'upload_image.html', {'error': 'Only image files are allowed.'})

        # Save image directly using the model
        uploaded_image = UploadedImage(image=uploaded_file)

        # Extract geolocation (latitude, longitude) from the image
        latitude, longitude = get_geolocation(uploaded_file)

        # If geolocation is found, save it to the model
        if latitude and longitude:
            uploaded_image.latitude = latitude
            uploaded_image.longitude = longitude
        else:
            uploaded_image.latitude = None
            uploaded_image.longitude = None

        # Perform OCR to extract text
        try:
            img = Image.open(uploaded_file)
            uploaded_image.extracted_text = pytesseract.image_to_string(img)
        except Exception as e:
            uploaded_image.extracted_text = f"Error processing image: {e}"

        # Save the extracted text and geolocation data to the database
        uploaded_image.save()

        return redirect(reverse_lazy('view_images'))



class ImageListView(View):

    def get(self, request):
        """Display a list of uploaded images and their extracted text."""
        images = UploadedImage.objects.all()
        return render(request, 'view_images.html', {'images': images})
