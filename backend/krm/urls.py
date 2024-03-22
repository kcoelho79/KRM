from django.urls import path
from .views import ContatoListView, ContatoCreateView, ContatoDetailView, ContatoUpdateView, ContatoDeleteView
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='krm/index.html'), name='index'),
    path('list', ContatoListView.as_view(), name='contato-list'),
    path('create/', ContatoCreateView.as_view(), name='contato-create'),
    path('<int:pk>/', ContatoDetailView.as_view(), name='contato-detail'),
    path('<int:pk>/update/', ContatoUpdateView.as_view(), name='contato-update'),
    path('<int:pk>/delete/', ContatoDeleteView.as_view(), name='contato-delete'),
]
