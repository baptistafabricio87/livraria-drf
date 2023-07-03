from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.views import APIView

from core.models import Categoria

import json


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):

    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao'] if 'descricao' in json_data else qs.descricao
        qs.save()
        data = {"id": qs.id, "descricao": qs.descricao}
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        data = {"mensagem": "Item excluído com sucesso!", "item": qs.descricao}
        qs.delete()
        return JsonResponse(data)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class CategoriaList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
