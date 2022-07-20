import speedtest
from datetime import datetime
import pandas as pd
from time import sleep
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

# Função para testar velocidade de conexão
def teste_internet():
    # Instanciando a função de test do Speedtest
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    # Testando velocidades
    velocidade_download = round(s.download(threads=None)*(10**-6))
    velocidade_upload = round(s.upload(threads=None)*(10**-6))
    # Capturando data e hora do teste
    data_atual = datetime.now().strftime('%d/%m/%Y')
    hora_atual = datetime.now().strftime('%H:%M')

    return data_atual, hora_atual, velocidade_download, velocidade_upload

def a():
# Definição de variáveis para teste
    quantidade_testes = 1
    intervalo_minutos = 0 
    segundos = 10
# Loop para execução dos testes
    for q in range(quantidade_testes):
        data_atual, hora_atual, velocidade_download, velocidade_upload = teste_internet()
        print('Teste {}/{} Data: {} Hora: {} Download: {} Upload: {}'.format(q+1, quantidade_testes, data_atual, hora_atual, velocidade_download, velocidade_upload))    
        if (q+1) < quantidade_testes:
            sleep(intervalo_minutos*segundos)

janela = Tk()

printar = Label(janela, text="")
printar.grid(column=0, row=1)

botao = Button(janela, text="Rodar", command=a)
botao.grid(column=0, row=3)
janela.mainloop()