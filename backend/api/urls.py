
from django.urls import path
from .views import ContatoListCreateAPIView, ContatoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('contatos/', ContatoListCreateAPIView.as_view(), name='contato-list-create'),
    path('contatos/<int:pk>/', ContatoRetrieveUpdateDestroyAPIView.as_view(), name='contato-detail'),
]
