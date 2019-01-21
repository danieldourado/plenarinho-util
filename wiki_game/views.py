from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import WikiGameForm
from .models import WikiGame

import csv

class WikiGameList(ListView):
    WikiGame.objects.all().delete()
    with open('wiki-game-data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            tempWiki = WikiGame()
            tempWiki.name = row['Termo']
            tempWiki.texto = row['Texto']
            tempWiki.save()
    
    model = WikiGame
    paginate_by = 20


class WikiGameCreate(CreateView):
    model = WikiGame
    form_class = WikiGameForm
    success_url = reverse_lazy('wiki_game:list')


class WikiGameDetail(DetailView):
    model = WikiGame


class WikiGameUpdate(UpdateView):
    model = WikiGame
    form_class = WikiGameForm
    success_url = reverse_lazy('wiki_game:list')


class WikiGameDelete(DeleteView):
    model = WikiGame
    success_url = reverse_lazy('wiki_game:list')
