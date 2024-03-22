from django.shortcuts import render
from rest_framework import generics
from krm.models import Contato
from .serializers import ContatoSerializer

class ContatoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

class ContatoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

