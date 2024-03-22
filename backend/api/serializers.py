from rest_framework import serializers
from krm.models import Contato

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'telefone', 'origem', 'email']
