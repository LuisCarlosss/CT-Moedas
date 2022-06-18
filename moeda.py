from webbrowser import get
import requests
import json



#Função de cotação de moeda
def get_coin(coin):
    #Site usado fazer requisição
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

    #Fazer requisição
    r = requests.get(url)
    j = r.json()

    #Cotação da moedas
    #USDBRL 'EURBRL' 'BTCBRL'
    dolar = j['USDBRL']['bid'][0:4]
    euro = j['EURBRL']['bid'][0:4]
    bitcoin = j['BTCBRL']['bid']
    
    #Estrutura de codição
    if coin == 1:
        print(f'Valor do dolar é {dolar}')
    elif coin == 2:
        print(f'Valor do Euro é {euro}')
    elif coin == 3:
        print(f'Valor do bitcoin é {bitcoin}')
    else:
        print('Moeda não encontrada!')

while True:     
    #Mostra opção
    print('''
    [1] Dolar
    [2] Euro
    [3] Bitcoin\n''')
    
    get_coin(int(input('Digite:')))
