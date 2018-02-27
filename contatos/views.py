from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#a função sempre recebe uma request e responde uma response
def index(request):
    pessoas =["Aurélindo"]
    return render(request,'lista.html',context={'bola':pessoas})

def detalhes(request, contatosId):
    return HttpResponse("Detalhes:")
