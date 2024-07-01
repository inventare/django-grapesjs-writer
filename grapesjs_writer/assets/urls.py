from django.urls import path
from .views import AssetUploadAPIView

app_name = 'grapesjs_assets'

urlpatterns = [
    path('upload/', AssetUploadAPIView.as_view(), name='upload'),
]
