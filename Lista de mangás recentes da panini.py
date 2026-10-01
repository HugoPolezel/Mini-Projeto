import time
import bs4
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://panini.com.br')

navegador.find_element("id", "close-modal").click()
time.sleep(2)

navegador.find_element("id", "ui-id-249").click()
time.sleep(5)

navegador.find_element("id", "sorter").send_keys("Mais recentes")
time.sleep(2)


html = navegador.page_source


sopa = bs4.BeautifulSoup(html, 'html.parser')
nomes = sopa.select('a.product-item-link')
precos = sopa.select('span.price')


for i in range(12):
    nome = nomes[i].text
    preco = precos[i].text
    print(nome)
    print(preco)
    print()

input('Pressione enter para fechar o navegador')