from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProjetoForm
from .models import Projeto
from projetos.plenarinho_crawler import *


class ProjetoList(ListView):
    model = Projeto
    paginate_by = 20

class ProjetoListForPDF(ListView):
    model = Projeto
    ordering = ['-tema']
    template_name = 'projetos/projeto_list_for_pdf.html'
    paginate_by = 1000


class ProjetoCreate(CreateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('projetos:list')


class ProjetoDetail(DetailView):
    model = Projeto


class ProjetoUpdate(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('projetos:list')


class ProjetoDelete(DeleteView):
    model = Projeto
    success_url = reverse_lazy('projetos:list')

def ProjetoCrawl(request):
    getProjetos()
    return HttpResponseRedirect(reverse_lazy('projetos:list'))

