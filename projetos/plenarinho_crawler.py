from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib.request
from .models import Projeto



def getProjetos():
    getLinks()
    extractProjetoDataFromLinks()

    
    
def extractProjetoDataFromLinks():
    
    projetos = Projeto.objects.all()
    
    for projeto in projetos:
        if projeto.name == '':
            extractProjetoData(projeto)
   
           
def extractProjetoData(projeto):

    r = urllib.request.urlopen(projeto.link)
    soup = BeautifulSoup(r, 'html.parser')
    infoBox = soup.find('div', attrs={'id':'infoBox'})
    
    projeto.name                = infoBox.find('nome').string
    projeto.nomeDaCrianca       = infoBox.find('nome').string
    projeto.sexo                = infoBox.find('sexo').string
    projeto.dataDeNascimento    = infoBox.find('datadenascimento').string
    projeto.endereco            = infoBox.find('endereco').string
    projeto.cidade              = infoBox.find('cidade').string
    projeto.uf                  = infoBox.find('uf').string
    projeto.cep                 = infoBox.find('cep').string
    projeto.telefone            = infoBox.find('telefone').string
    projeto.email               = infoBox.find('email').string
    projeto.escola              = infoBox.find('escola').string
    projeto.serie               = infoBox.find('serie').string
    projeto.nomeDosPais         = infoBox.find('nomedospais').string
    projeto.nomeDoProjetoDeLei  = infoBox.find('nomedoprojetodelei').string
    projeto.tema                = infoBox.find('tema').string
    projeto.projetoDeLei        = infoBox.find('projetodelei').string
    projeto.justificativa       = infoBox.find('justificativa').string
    projeto.ano                 = infoBox.find('ano').string
    projeto.save()
    print("finished "+projeto.name)
        
def getLinks():
    
    result = Projeto.objects.filter(link__contains='/')
    
    if result.count() != 0:
        return;
    
    list_of_links = []
    for x in range(1,4):
        list_of_links += getLinkAdressFromPage('https://plenarinho.leg.br/index.php/listar-todos-os-projetos-de-lei-publicados/?vpage='+str(x))
    
    saveLinks(list_of_links)
    
    
def saveLinks(links):
    for link in links:
        projeto = Projeto.objects.create()
        projeto.link = link
        projeto.save()
    
def getLinkAdressFromPage(page_address):
    list_of_links = []
    r = urllib.request.urlopen(page_address)
    soup = BeautifulSoup(r, 'html.parser')
    
    div = soup.find('article', attrs={'class':'itemscope post_item post_item_single post_featured_default post_format_standard post-7624 page type-page status-publish hentry'})
    a_tags = div.find_all('a', attrs={'class':'_self', 'target':'_self'})

    for a_tag in a_tags:
        list_of_links.append(a_tag.get('href'))
    
    return list_of_links