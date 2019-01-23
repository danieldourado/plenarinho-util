from .models import WikiGame, WikiTermos
import csv

termo_splitter = "*"
termo_LI = "["
termo_RI = "]"

def refresh_wikigame_model():
    WikiGame.objects.all().delete()
    dataset = extract_data_from_csv()
    save_termos(dataset)
    save_wikigame(dataset)

def save_wikigame(dataset):
    for data in dataset:
        tempWikiGame = WikiGame()
        tempWikiGame.name = WikiTermos.objects.get(name=data['termo'])
        tempWikiGame.texto = data['texto']
        termos = extract_termos_from_string(data['out_links'])
        tempWikiGame.save()
        tempWikiGame.out_links_set.add(*termos)
        tempWikiGame.save()

def extract_termos_from_string(dataset):
    termos_list = []
    strings_termos = dataset.split(termo_splitter)
    for string_termo in strings_termos:
        if string_termo == '': 
            continue
        if termo_LI not in string_termo:
            termo = string_termo
        else:
            termo = string_termo[string_termo.find(termo_LI)+1:string_termo.find(termo_RI)]
        
        termo = termo.rstrip().lstrip()
        print('looking for termo', termo)
        temp_termo = WikiTermos.objects.get(name__iexact=termo)
        termos_list.append(temp_termo)
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