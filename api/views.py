from rest_framework import generics
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from api.models import EmpresaSerializer
from enviame.models import Empresa


class EmpresaListar(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaListarAPIView(ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaCrearAPIView(CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaEditarAPIView(UpdateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaEliminarAPIView(DestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
