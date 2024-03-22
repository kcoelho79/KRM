from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Contato

class ContatoListView(ListView):
    model = Contato
    template_name = 'krm/contato_list.html'
    context_object_name = 'contatos'

class ContatoCreateView(CreateView):
    model = Contato
    template_name = 'krm/contato_form.html'
    fields = ['nome', 'telefone', 'origem', 'email']
    success_url = reverse_lazy('contato-list')

class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'krm/contato_detail.html'
    context_object_name = 'contato'

class ContatoUpdateView(UpdateView):
    model = Contato
    template_name = 'krm/contato_form.html'
    fields = ['nome', 'telefone', 'origem', 'email']
    context_object_name = 'contato'

    def get_success_url(self):
        return reverse_lazy('contato-detail', kwargs={'pk': self.object.pk})

class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = ''
    success_url = reverse_lazy('contato-list')
