from .models import WikiGame, WikiTermos
import csv

termo_splitter = "*"
termo_LI = "["
termo_RI = "]"

def refresh_wikigame_model():
    WikiGame.objects.all().delete()
    WikiTermos.objects.all().delete()
    dataset = extract_data_from_csv()
    save_termos(dataset)
    save_wikigame(dataset)

def save_wikigame(dataset):
    for data in dataset:
        tempWikiGame = WikiGame()
        tempWikiGame.name = data['termo']
        tempWikiGame.texto = data['texto']
        termos = extract_termos_from_string(data['out_links'])
        tempWikiGame.save()
        tempWikiGame.out_links_set.add(*termos)
        tempWikiGame.save()

def extract_termos_from_string(dataset):
    termos_list = []
    strings_termos = dataset.split(termo_splitter)
    for string_termo in strings_termos:
        alias_in_text = ""
        termo = ""
        if string_termo == '': 
            continue
        if termo_LI not in string_termo:
            termo = string_termo
        else:
            termo = string_termo[string_termo.find(termo_LI)+1:string_termo.find(termo_RI)]
            alias_in_text = string_termo.partition("[")[0]
        
        termo = termo.rstrip().lstrip()
        if alias_in_text:
            alias_in_text = alias_in_text.rstrip().lstrip()
        else:
            alias_in_text = termo
            
        tempWikiTermos = WikiTermos()
        tempWikiTermos.name = termo
        tempWikiTermos.alias_in_text = alias_in_text
        tempWikiTermos.save()
    
        
        termos_list.append(tempWikiTermos)
    return termos_list

def extract_data_from_csv():
    data = []
    with open('wiki-game-data.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            tempWiki = {}
            tempWiki['termo'] = row['Termo']
            tempWiki['texto'] = row['Texto']
            tempWiki['out_links'] = row['Out']
            data.append(tempWiki)
    return data
    
def save_termos(dataset):
    for data in dataset:
        tempWikiTermos = WikiTermos()
        tempWikiTermos.name = data['termo']
        tempWikiTermos.save()