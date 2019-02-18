from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from .forms import WikiGameForm
from .models import WikiGame
from .csv_data_extracter import refresh_wikigame_model
import csv
from django.shortcuts import redirect
from django.core.serializers import serialize
import json

def extract_data_from_csv(request):
    refresh_wikigame_model()
    return redirect('/wikigame/list/')
    
class HomeGameView(TemplateView):

    template_name = "wikigame/wikigame_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        values =  WikiGame.objects.all()
        
        obj_list = []
        
        for value in values:
            temp_obj = {
                "name":value.name,
                "imagem":value.imagem,
                "texto":value.texto.replace('"','')
            }
            temp_out_links = []
            for item in value.out_links_set.all():
                temp_out_links.append({"name":item.name, "alias_in_text":item.alias_in_text})
            temp_obj['out_links'] = temp_out_links
            obj_list.append(temp_obj)

        context['latest_articles'] = json.dumps(obj_list)
        
        return context
    
class InstructionsGameView(TemplateView):

    template_name = "wikigame/wikigame_instructions.html"

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
