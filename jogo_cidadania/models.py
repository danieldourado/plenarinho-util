from django.core.urlresolvers import reverse
from django.db import models


class Falas(models.Model):
    name = models.CharField(max_length=255)
    texto= models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jogo_cidadania:detail', args=[str(self.id)])
