from django.db import transaction
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import AssetUploadSerializer, AssetItemRetrieveSerializer
from .models import AssetItem

class AssetUploadAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def _create_item(self, file: InMemoryUploadedFile, template_model_class: str):
        return AssetItem.objects.create(
            template_model_class=template_model_class,
            image=file,
        )

    def post(self, request):
        serializer = AssetUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        template_model_class = serializer.validated_data.get('template_model_class')
        files = serializer.validated_data.get('files')
        
        with transaction.atomic():
            assets = list(map(lambda file: self._create_item(file, template_model_class), files))

        serializer = AssetItemRetrieveSerializer(assets, many=True)
        return Response({
            'data': serializer.data,
        })
