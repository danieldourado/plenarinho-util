from django.shortcuts import render
from django.views.generic import TemplateView
import requests

class ContagemVotos(TemplateView):
    template_name = 'votos/votos_list.html'
    
    def get_context_data(self, **kwargs):
        URL = "https://j9zfp6zmth.execute-api.us-east-1.amazonaws.com/test/mydemoresource"
        PARAMS = {} 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        
        numeros = {}
        
        for item in data['Items']:
            current_numero = item['numero']['S']
            if not current_numero in numeros:
                numeros[current_numero] = 0
            numeros[current_numero] += 1
        sorted_by_value = sorted(numeros.items(), key=lambda kv: kv[1], reverse=True)
        print(str(sorted_by_value[0][0]))
        
        total = 0
        for voto in sorted_by_value:
            total += voto[1]
        context = {"votos_list":sorted_by_value, 'votos_total':total}
        return context