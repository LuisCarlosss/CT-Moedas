
import requests
import json
import PySimpleGUI as sg



#Sistema 

url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

#Fazer requisição
r = requests.get(url)
j = r.json()

#Cotação da moedas
#USDBRL 'EURBRL' 'BTCBRL'
dolar = j['USDBRL']['bid'][0:4]
euro = j['EURBRL']['bid'][0:4]
bitcoin = j['BTCBRL']['bid']


#Menu
sg.theme('DarkBrown')
tela = [
    [sg.Text('Cotação de moeda')],
    [sg.Button('Dolar',key='Dolar'),sg.Button('Euro',key='Euro'),sg.Button('Bitcoin',key='Bitcoin')],
    [sg.Text('',key='resposta')]
]


janela = sg.Window('Sistema de cotação de moeda',tela,size=(200,120))

while True:
    evento,valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        print('Saindo do sistema...')
        break
    if evento == 'Dolar':janela['resposta'].update(f'Valor do Dolar é {dolar}')
    elif evento == 'Euro':
        janela['resposta'].update(f'Valor do Euro é {euro}')
    elif evento == 'Bitcoin':
        janela['resposta'].update(f'Valor do Bitcoin é {bitcoin}')

janela.close()