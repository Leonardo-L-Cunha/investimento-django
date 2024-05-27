from django.shortcuts import render
from django.shortcuts import HttpResponse

def investimentos(request):
    return HttpResponse('Vamos investir')


def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento = {
        'tipo_investimento': request.POST.get('tipoInvestimento')
    }
    return render(request, 'investimentos/investimento_registrado.html', investimento)