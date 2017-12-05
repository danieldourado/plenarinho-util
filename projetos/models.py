from django.core.urlresolvers import reverse
from django.db import models


class Projeto(models.Model):
    name                = models.CharField(max_length=255)
    nomeDaCrianca       = models.CharField(max_length=255)
    sexo                = models.CharField(max_length=255)
    dataDeNascimento    = models.CharField(max_length=255)
    endereco            = models.CharField(max_length=255)
    cidade              = models.CharField(max_length=255)
    uf                  = models.CharField(max_length=255)
    cep                 = models.CharField(max_length=255)
    telefone            = models.CharField(max_length=255)
    email               = models.CharField(max_length=255)
    escola              = models.CharField(max_length=255)
    serie               = models.CharField(max_length=255)
    nomeDosPais         = models.CharField(max_length=255)
    nomeDoProjetoDeLei  = models.CharField(max_length=255)
    tema                = models.CharField(max_length=255)
    projetoDeLei        = models.TextField()
    justificativa       = models.TextField()
    ano                 = models.CharField(max_length=255)
    link                = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projetos:detail', args=[str(self.id)])

