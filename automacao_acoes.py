import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# digite o código "PETR4.SA" disponível no site da Yahoo ou da ação que você quiser
ticker = input("Digite o código da ação desejada: ").upper()


dados = yfinance.Ticker(ticker).history(start="2023-01-01", end="2023-12-31")
fechamento = dados.Close

minimo = round(fechamento.min(), 2)
maximo = round(fechamento.max(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "analistadesistemasedilson@gmail.com"
assunto = "Análises do Projeto da Petrobrás 2023"
mensagem = f"""
Prezado Gestor,

Segue as análises solicitadas da ação {ticker}:

Cotação mínima: R$ {minimo}
Cotação máxima: R$ {maximo}
Valor médio: R$ {valor_medio}

Qualquer dúvida, estou à disposição!

Atte,

Edilson Freire
Analista de Sistemas
"""

# abrir o navegador e ir para o gmail
webbrowser.open('https://www.gmail.com')
time.sleep(8)

# configurando uma pausa de 3 segundo para cada comando
pyautogui.PAUSE = 3

# clicar no botao escrever
pyautogui.click(104, 180)

# digitar o email do destinatario e clicar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto e clicar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# digitar a mensagem e clicar TAB
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

# clicar no botao enviar
pyautogui.hotkey("enter")

# fechar a aba do navegador
pyautogui.hotkey("ctrl","f4")

print("\nMensagem enviada com sucesso!\n")