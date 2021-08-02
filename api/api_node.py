import requests
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class ConsumirApiNode(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'empresa/crear.html'

    def get(self, request):
        url ='http://localhost:8080/listar'
        response = requests.get(url)
        data = response.json()
        return Response(data)

