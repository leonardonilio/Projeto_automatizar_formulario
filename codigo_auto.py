from selenium import webdriver
import pyautogui as py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas
import keyboard

# abrir o navegador
navegador = webdriver.Chrome()

# acessar um site
navegador.get("https://projetoautomatizarformulario-szfhwngpahrpaabivomfuk.streamlit.app/")

# colocar o navegador em tela cheia
navegador.maximize_window()

#espera para carregar
time.sleep(25) 

#preenche os campos para o login
py.click(x=966, y=253) # clica na tela para preencher o proximo campo
py.press("tab")
py.write("Usuario@gmail.com")
py.press("tab")
py.write("M!@@#0923l")

#Abre a proxima tela
py.press("tab")
py.press("tab")
py.press("enter")
time.sleep(50)

#Abre o banco de dados
tabela = pandas.read_csv("produtos.csv")


#preenche o formulario em um loop

            #linha se repete enquanto tiver index no banco de dados
for linha in tabela.index:
    
    #Um "freio" para o for ao apertar a tecla q (pode ser necessario clicar mais de uma vez)
    if keyboard.is_pressed("q"):
        print("Processo interrompido pelo usuário.")
        break
    
    #clica na tela para poder ir no proximo campo
    py.click(x=861, y=255)#Ajusta o mouse para as cordenadas especificadas
    py.press("tab")
    codigo = str(tabela.loc[linha, "codigo"]) # seleciona o item da coluna referida entre "" na linha atual da tabela
    py.write(codigo)
    py.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    py.write(marca)
    py.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    py.write(tipo)
    py.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    py.write(categoria)
    py.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    py.write(preco_unitario)
    py.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    py.write(custo)
    py.press("tab")

    #Como nem todo item precisa de observações, isso pode tem que ser tratato já que "nan" não
    #pode ser convertido para String
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":#"nan" é similar a nulo
        py.write(obs)
    
    py.press("tab")

    py.press("enter")
   
    py.scroll(50000)#Faz um scroll para o topo da pagina
    
    time.sleep(4) #Uma pequena pausa para evitar travamento
time.sleep(10000)#Um tempo para poder observar o que foi colocado no site
