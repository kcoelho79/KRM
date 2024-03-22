from django.db import models

class Contato(models.Model):
    ORIGEM_CHOICES = (
        ('form', 'Formulário'),
        ('ligacao', 'Ligação'),
        ('messenger', 'Messenger'),
        ('visita', 'Visita'),
    )

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    origem = models.CharField(max_length=20, choices=ORIGEM_CHOICES, default='form')
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome