from rest_framework.viewsets import ModelViewSet

from core.serializers import CompraSerializer
from core.models import Compra


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
