# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://ncarbajal-automacao.vercel.app/
import pyautogui
import time

# pyautogui.write -> escrever um texto 
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#pyautogui.click(x=702, y=29, clicks=2)

# entrar no link 
pyautogui.write("https://ncarbajal-automacao.vercel.app/")
pyautogui.press("enter")
time.sleep(1.5)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=834, y=513)
# escrever o seu email
pyautogui.write("flamengo@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("123456")
pyautogui.press("tab")# passa para o botao de login
pyautogui.press("tab")# passa para o botao de login
pyautogui.press("tab")# passa para o botao de login
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("./produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=775, y=502)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")# cadastra o produto (botao enviar)
    pyautogui.press("tab")
    pyautogui.press("enter")# limpa tabela
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fimpythonimpressionador@gmail.com   sua senha