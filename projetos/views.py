# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProjetoForm
from .models import Projeto
from projetos.plenarinho_crawler import *
import csv


class ProjetoList(ListView):
    model = Projeto
    paginate_by = 20

class ProjetoListForPDF(ListView):
    model = Projeto
    ordering = ['-tema']
    template_name = 'projetos/projeto_list_for_pdf.html'
    paginate_by = 167


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

def ProjetoExtractEnderecoParticipantes(request):
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Endereço dos autores de projetos de lei.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    writer.writerow([smart_str(u'Nome'), smart_str(u'Endereço'), smart_str(u'Cidade'), smart_str(u'Estado'), smart_str(u'CEP')])
    
    #projetos = Projeto.objects.all()
    projetos = Projeto.objects.order_by('nomeDaCrianca').distinct('nomeDaCrianca')

    
    
    for projeto in projetos:
        writer.writerow([smart_str(projeto.nomeDaCrianca), smart_str(projeto.endereco), smart_str(projeto.cidade), smart_str(projeto.uf), smart_str(projeto.cep)])

    return response