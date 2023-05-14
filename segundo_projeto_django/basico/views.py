from django.shortcuts import render
from django.http import HttpResponse
# Todas as funções estão associadas a um url que é apontado no arquivo url.py na urlpatterns - é a 
# lista de todas as urls.


# def inicio(request):
#     resposta = HttpResponse('página inicial')
#     return resposta

def inicio(request):
    # A função render irá transforma o documento html em uma string.
    dados = []
    dados.append(
    {
        'Titulo': 'Olá mundo estou a caminho',
        'Categoria':'Desenvolverdor python',
        'Data': '10/05/2023',

    }
    )
    dados.append(
      {
        'Titulo': 'Estou aprendendo com a vida.',
        'Categoria':'aprender',
        'Data': '15/05/2023',
    
    }

    )
    contexto  = {
        'dados':dados
    }
    resposta = render(request, 'primeiro.html', contexto)
    return resposta



def contato(request):
   resposta = render(request,'pagina_de_contato.html')
   
   return resposta