from django.conf.urls import url, include
from . import views
from trivia.models import *
from trivia.resources import start_export
from rest_framework import serializers, viewsets, routers

        
class SaibaMaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaibaMais
        fields = '__all__'
        
class OpcaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcao
        fields = '__all__'

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'

class EtapaSerializer(serializers.ModelSerializer):
    pergunta = PerguntaSerializer(read_only=True)
    resposta = PerguntaSerializer(read_only=True)
    opcao_set = OpcaoSerializer(many=True, read_only=True)
    saiba_mais = SaibaMaisSerializer(read_only=True)
    
    class Meta:
        model = Etapa
        fields = ('pergunta', 'resposta','opcao_set','saiba_mais')

# Serializers define the API representation.
class TriviaSerializer(serializers.ModelSerializer):
    etapa_set = EtapaSerializer(many=True, read_only=True)

    class Meta:
        model = Trivia
        fields = ('name', 'etapa_set')


# ViewSets define the view behavior.
class TriviaViewSet(viewsets.ModelViewSet):
    queryset = Trivia.objects.all()
    serializer_class = TriviaSerializer

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'trivias', TriviaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^import', start_export),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
