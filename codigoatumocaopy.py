import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

#abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#abrindo o site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2)
#fazendo o login no site
pyautogui.click(x=590, y=396)
pyautogui.write("marciojucelio@gmail.com")
pyautogui.click(x=662, y=495)
pyautogui.write("12345678")
pyautogui.click(x=675, y=566)

#lendo a base de dados
table = pandas.read_csv("produtos.csv")
print(table)

time.sleep(2)
#cadastrando produtos
for linha in table.index:
    codigo = table.loc[linha, "codigo"]
    marca = table.loc[linha, "marca"]
    tipo = table.loc[linha, "tipo"]
    categoria = table.loc[linha, "categoria"]
    preco = table.loc[linha, "preco_unitario"]
    custo = table.loc[linha, "custo"]
    

    pyautogui.click(x=686, y=279)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = table.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")

    #enviando produtos
    pyautogui.press("enter")

    #cadastrando um novo produto
    pyautogui.scroll(5000)