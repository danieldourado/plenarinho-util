from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .forms import WikiGameForm
from .models import WikiGame
from .csv_data_extracter import refresh_wikigame_model
import csv
from django.shortcuts import redirect

def extract_data_from_csv(request):
    refresh_wikigame_model()
    return redirect('/wikigame/list/')
    
class HomeGameView(TemplateView):

    template_name = "wikigame/wikigame_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = WikiGame.objects.all()
        return context

    

class WikiGameList(ListView):
    model = WikiGame
    paginate_by = 20


class WikiGameCreate(CreateView):
    model = WikiGame
    form_class = WikiGameForm
    success_url = reverse_lazy('wikigame:list')


class WikiGameDetail(DetailView):
    model = WikiGame


class WikiGameUpdate(UpdateView):
    model = WikiGame
    form_class = WikiGameForm
    success_url = reverse_lazy('wikigame:list')


class WikiGameDelete(DeleteView):
    model = WikiGame
    success_url = reverse_lazy('wikigame:list')
