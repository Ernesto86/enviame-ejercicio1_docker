from enviame.models import Empresa
from rest_framework import serializers


# Create your models here.
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
