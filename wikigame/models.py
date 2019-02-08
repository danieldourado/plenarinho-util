from django.core.urlresolvers import reverse
from django.db import models


class WikiTermos(models.Model):
    name = models.CharField(max_length=255)
    alias_in_text = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.name

class WikiGame(models.Model):
    name = models.CharField(max_length=255)
    texto = models.TextField(default='')
    out_links_set = models.ManyToManyField(WikiTermos, related_name="out_links", verbose_name="Out Links")
    
    def __str__(self):
        return self.name.name

    def get_absolute_url(self):
        return reverse('wikigame:detail', args=[str(self.id)])