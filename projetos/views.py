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
    
def ProjetoExtractEmail(request):
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Endereço de email dos autores de projetos de lei.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    writer.writerow([smart_str(u'Nome'), smart_str(u'Email')])
    
    #projetos = Projeto.objects.all()
    projetos = Projeto.objects.order_by('nomeDaCrianca').distinct('nomeDaCrianca')
    
    for projeto in projetos:
        writer.writerow([smart_str(projeto.nomeDaCrianca), smart_str(projeto.email)])

    return response

def ProjetoExtractDados(request):
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Dados dos autores de projetos de lei.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    writer.writerow([
        smart_str(u'Nome'),
        smart_str(u'Sexo'),
        smart_str(u'dataDeNascimento'),
        smart_str(u'cidade'),
        smart_str(u'uf'),
        smart_str(u'telefone'),
        smart_str(u'email'),
        smart_str(u'escola'),
        smart_str(u'serie'),
        smart_str(u'nomeDosPais'),
        smart_str(u'nomeDoProjetoDeLei'),
        smart_str(u'tema'),
        smart_str(u'projetoDeLei'),
        smart_str(u'justificativa'),
        smart_str(u'ano'),
        smart_str(u'link'),
        smart_str(u'responsavel'),
        ])

    #projetos = Projeto.objects.all()
    projetos = Projeto.objects.order_by('nomeDaCrianca').distinct('nomeDaCrianca')
    
    for projeto in projetos:
        writer.writerow([
            
            
            
            smart_str(projeto.nomeDaCrianca),
            smart_str(projeto.sexo),
            smart_str(projeto.dataDeNascimento),
            smart_str(projeto.cidade),
            smart_str(projeto.uf),
            smart_str(projeto.telefone),
            smart_str(projeto.email),
            smart_str(projeto.escola),
            smart_str(projeto.serie),
            smart_str(projeto.nomeDosPais),
            smart_str(projeto.nomeDoProjetoDeLei),
            smart_str(projeto.tema),
            smart_str(projeto.projetoDeLei),
            smart_str(projeto.justificativa),
            smart_str(projeto.ano),
            smart_str(projeto.link),
            smart_str(projeto.responsavel),
        ])

    return response