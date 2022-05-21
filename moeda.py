import requests
import json

#Site usado fazer requisição
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

#Função de cotação de moeda
def moeda(moeda):
    #Fazer requisição
    r = requests.get(url)
    j = r.json()

    #Cotação da moedas
    #USDBRL 'EURBRL' 'BTCBRL'
    dolar = j['USDBRL']['bid']
    euro = j['EURBRL']['bid']
    bitcoin = j['BTCBRL']['bid']
    
    #Condições 
    if moeda == 1:
        return f'Valor do Dolar é R$ {dolar}'
    elif moeda == 2:
        return f'Valor do Euro é R$ {euro}'
    elif moeda == 3:
        return f'Valor do Bitcoin é R$ {bitcoin}'
    else:
        print('Moeda Não encontrada!')
        print('Tente novamente!')
        
#loop infinito
while True: 
    #Opções 
    print(moeda(int(input('''
    [1] Dolar
    [2] Euro
    [3] Bitcoin

    Digite:'''))))
    continue