from django.core.urlresolvers import reverse
from django.db import models


class WikiGame(models.Model):
    name = models.CharField(max_length=255)
    texto = models.TextField(default='', null=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wiki_game:detail', args=[str(self.id)])
