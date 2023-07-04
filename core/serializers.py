from rest_framework.serializers import ModelSerializer

from core.models import Categoria


# Serializer
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
