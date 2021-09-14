import csv
from trivia.models import Etapa, Opcao, Pergunta, SaibaMais, Trivia

def get_resposta(gabarito, opcoes):
    if gabarito == 'a':
        return opcoes[0]
    if gabarito == 'b':
        return opcoes[1]
    if gabarito == 'c':
        return opcoes[2]
    if gabarito == 'd':
        return opcoes[3]
    return None

def start_export(request):
    NOME = "Internet segura"
    perguntas = set()
    opcao_a = set()
    opcao_b = set()
    opcao_c = set()
    opcao_d = set()
    respostas = set()
    saiba_mais = set()

    
    with open('trivia/exported_items.csv', newline='') as csvfile:
     spamreader = csv.DictReader(csvfile)
     etapas = set()
     for row in spamreader:
         pergunta = Pergunta(texto=row["Pergunta"])
         pergunta.save()
         opcao_a = Opcao(texto=row['Opção "a"'])
         opcao_b = Opcao(texto=row['Opção "b"'])
         opcao_c = Opcao(texto=row['Opção "c"'])
         opcao_d = Opcao(texto=row['Opção "d"'])
         resposta = get_resposta(row['Resposta'], [opcao_a, opcao_b, opcao_c, opcao_d])
         resposta.save()
         opcao_a.save()
         opcao_b.save()
         opcao_c.save()
         opcao_d.save()
         saiba_mais = SaibaMais(texto=row['Saiba Mais'])
         saiba_mais.save()
         
         etapa = Etapa(pergunta=pergunta, resposta=resposta, saiba_mais=saiba_mais)
         etapa.save()
         opcoes = (opcao_a, opcao_b, opcao_c, opcao_d) if opcao_d.texto != '' else (opcao_a, opcao_b, opcao_c)
         etapa.opcao_set = opcoes
         etapas.add(etapa)
    trivia = Trivia(name=NOME)
    trivia.save()
    trivia.etapa_set = etapas
    print(trivia)