import random

from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect
from faker import Faker
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import EmpresaSerializer
from enviame.models import Empresa


class EmpresaIndex(APIView):
    def get(self, request):
        return redirect('/api/v1/listar')


class EmpresaListarView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'empresa/listar.html'

    def get(self, request):
        search = self.request.GET.get('s', '')
        empresas = Empresa.objects.filter(
            Q(estado=True),
            Q(nombre__icontains=search)
        )
        return Response({'empresas': empresas, 's': search})


class EmpresaCrearView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'empresa/crear.html'

    def get(self, request):
        serializer = EmpresaSerializer()
        return Response({'serializer': serializer, 'accion': 'Crear'})

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/')


class EmpresaEditarView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'empresa/editar.html'

    def get(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        serializer = EmpresaSerializer(empresa)
        return Response({'serializer': serializer, 'empresa': empresa, 'accion': 'Editar'})

    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        serializer = EmpresaSerializer(empresa, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'empresa': empresa, 'accion': 'Editar'})
        serializer.save()
        return redirect('/')


class EmpresaEliminarView(APIView):
    def get(self, request, pk):
        with transaction.atomic():
            empresa = get_object_or_404(Empresa, pk=pk)
            empresa.estado = False
            empresa.save()
            return redirect('/')


class EmpresaFakerView(APIView):
    def get(self, request, n):
        with transaction.atomic():
            fake = Faker()
            tipo = ('PRIVADA', 'PUBLICA')
            for i in range(n):
                empresa = Empresa(
                    codigo=fake.postcode(),
                    nombre=fake.company(),
                    tipo=tipo[random.randrange(len(tipo))],
                    ciudad=fake.city(),
                    representante=fake.name()
                )
                empresa.save()
            return redirect('/')
