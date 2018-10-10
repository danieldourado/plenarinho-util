from lxml import html
import requests
from bs4 import BeautifulSoup
import urllib.request
from .models import Projeto

def getProjetos():
    #Projeto.objects.all().delete()
    #getLinks()
    extractProjetoDataFromLinks()

def extractProjetoDataFromLinks():
    
    projetos = Projeto.objects.all()
    for projeto in projetos:
        if projeto.name == '':
            if not extractProjetoData(projeto):
                print('Projeto deu erro: ', str(projeto.link))
                return
            
def extractProjetoData(projeto):

    infoBox = get_projeto(projeto)
    if not infoBox:
        return
    
    #projeto = Projeto.objects.create()
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
    try:
        projeto.save()
        print("finished "+projeto.name)
    except Exception as e:
        print (str(e))
        return False
    
    return True
    #projeto.delete()

def get_projeto(projeto, depth=1):
    try:
        r = urllib.request.urlopen(projeto.link)
        soup = BeautifulSoup(r, 'html.parser')
        infoBox = soup.find('div', attrs={'id':'infoBox'})
        nome = infoBox.find('nome').string
        return infoBox
    except Exception as e:
        depth += 1
        if depth > 5:
            return False
        print('error', str(projeto.link))
        return get_projeto(projeto, depth)
        
def getLinks():
    
    #url = 'https://plenarinho.leg.br/index.php/listar-todos-os-projetos-de-lei-publicados/?vpage='
    url = 'https://plenarinho.leg.br/index.php/category/camara-mirim/projetos-2018-camara-mirim/page/'
    '''
    result = Projeto.objects.filter(link__contains='/')
    
    if result.count() != 0:
        return;
    '''
    list_of_links = []
    for x in range(1,82):
        urls = getLinkAdressFromPage(url+str(x))
        list_of_links += urls
        print('added all projects from page ', str(x))
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
    
    #div = soup.find('article', attrs={'class':'itemscope post_item post_item_single post_featured_default post_format_standard post-7624 page type-page status-publish hentry'})
    #a_tags = div.find_all('a', attrs={'class':'_self', 'target':'_self'})
    divs = soup.find_all('h3', attrs={'class':'post_title'})
    #a_tags = div.find_all('a')

    for div in divs:
        list_of_links.append(div.find('a').get('href'))
    
    return list_of_links