from django.contrib import admin
from .models import *

admin.site.register([Trivia, Pergunta, Opcao, SaibaMais, Etapa])
