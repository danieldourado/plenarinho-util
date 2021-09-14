from django.core.urlresolvers import reverse
from django.db import models


class Projeto(models.Model):
    name                = models.TextField()
    nomeDaCrianca       = models.TextField()
    sexo                = models.TextField()
    dataDeNascimento    = models.TextField()
    cidade              = models.TextField()
    uf                  = models.TextField()
    telefone            = models.TextField()
    email               = models.TextField()
    escola              = models.TextField()
    serie               = models.TextField()
    nomeDosPais         = models.TextField()
    nomeDoProjetoDeLei  = models.TextField()
    tema                = models.TextField()
    projetoDeLei        = models.TextField()
    justificativa       = models.TextField()
    ano                 = models.TextField()
    link                = models.TextField()
    como_chegou         = models.TextField(null=True)
    responsavel         = models.TextField(null=True)
    parentesco          = models.TextField(null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projetos:detail', args=[str(self.id)])

