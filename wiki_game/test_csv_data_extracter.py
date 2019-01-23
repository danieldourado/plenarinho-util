from django.test import TestCase
from .models import WikiGame, WikiTermos
from .csv_data_extracter import extract_data_from_csv, save_termos, save_wikigame, extract_termos_from_string, refresh_wikigame_model

class CSVDETestCase(TestCase):
    mockup = {}
    def setUp(self):
        self.mockup = [
            {"termo":"cidadão","texto":"texto1 estados candidatos","out_links":"*estados[estado]*Poder Legislativo *candidatos[candidato]"},
            {"termo":"estado","texto":"texto1 cidadãos","out_links":"*cidadãos[cidadão]"},
            {"termo":"candidato","texto":"texto1 cidadãos","out_links":"*Poder Legislativo"},
            {"termo":"Poder Legislativo","texto":"texto1 cidadãos","out_links":"*cidadãos[cidadão]"}]
        
    def test_extract_data_from_csv(self):
        data = extract_data_from_csv()
        self.assertTrue(data)
    
    def test_save_termos(self):
        
        save_termos(self.mockup)
        print("Termos salvos:")
        for termo in WikiTermos.objects.all():
            print(termo.name)
        self.assertEqual(WikiTermos.objects.all().count(), len(self.mockup))
    
    def test_extract_termos_from_string(self):
        save_termos(self.mockup)
        termos = extract_termos_from_string(self.mockup[0]['out_links'])
        self.assertEqual(len(termos),3)
    
    def test_save_wikigame(self):
        save_termos(self.mockup)
        save_wikigame(self.mockup)
        self.assertEqual(WikiGame.objects.all().count(), len(self.mockup))
        
    def test_refresh_wikigame_model(self):
        refresh_wikigame_model()
        self.assertTrue(WikiGame.objects.all().count() != 0)