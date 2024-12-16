"""
URL configuration for agritech_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views.ImageUpload import ImageUploadView, ImageListView
from .views.home import Home
from .views.GeoJSON import GeoJSONView
from .views.ImageDelete import ImageDeleteView
from .views.MapView import MapView
from agritech_project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('upload/', ImageUploadView.as_view(), name='upload_image'),
    path('images/', ImageListView.as_view(), name='view_images'),
    path('geojson/', GeoJSONView.as_view(), name='geojson_data'),
    path('map/', MapView.as_view(), name='map'),
    path('delete/<int:image_id>/', ImageDeleteView.as_view(), name='delete_image')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
