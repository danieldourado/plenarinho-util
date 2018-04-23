from django.core.urlresolvers import reverse
from django.db import models


class Trivia(models.Model):
    name = models.CharField(max_length=255)
    etapa_set = models.ManyToManyField('trivia.Etapa', related_name="etapa", verbose_name="Etapas")
    
    def __str__(self):
        return self.name[:90]

    def get_absolute_url(self):
        return reverse('trivia:detail', args=[str(self.id)])

class Pergunta(models.Model):
    texto = models.TextField(default='', null=True)

    def __str__(self):
        return self.texto[:90]

class Opcao(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto[:90]
    class Meta:
        verbose_name_plural = "Opções"
class SaibaMais(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto[:90]

    class Meta:
        verbose_name_plural = "Saiba Mais"

class Etapa(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name="pergunta", null=True)
    resposta = models.ForeignKey(Opcao, related_name="resposta", null=True)
    opcao_set = models.ManyToManyField(Opcao, related_name="opcoes", verbose_name="Opções")
    saiba_mais = models.ForeignKey(SaibaMais, verbose_name="Saiba mais")
    def __str__(self):
        return self.pergunta.texto[:90]
    