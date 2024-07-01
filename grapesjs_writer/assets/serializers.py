from rest_framework import serializers
from .models import AssetItem

class AssetItemRetrieveSerializer(serializers.ModelSerializer):
    src = serializers.ImageField(source='image')
    name = serializers.CharField(source='display_name')

    class Meta:
        model = AssetItem
        fields = ["src", 'name']

class AssetUploadSerializer(serializers.Serializer):
    # TODO: add validators
    files = serializers.ListField(child=serializers.FileField())
    template_model_class = serializers.CharField()
