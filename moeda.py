import requests
import json

#Site para fazer requisição
url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

def moeda():
    #Fazer requisição
    r = requests.get(url)
    j = r.json()

    #USDBRL 'EURBRL' 'BTCBRL'
    dolar = j['USDBRL']['bid']
    euro = j['EURBRL']['bid']
    bitcoin = j['BTCBRL']['bid']
    
    return'''
    Valor do Dolar é R$ {}
    Valor do Euro é R$ {} 
    Valor do Bitcoin é R$ {} '''.format(dolar,euro,bitcoin)

print(moeda())