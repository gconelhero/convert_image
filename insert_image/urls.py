from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('uploaded/', views.uploaded_images, name='uploaded_images'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
