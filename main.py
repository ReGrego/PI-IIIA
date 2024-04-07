import requests
from bs4 import BeautifulSoup
#import mysql.connector

#conexao = mysql.connector.connect(user='root', password='', host='localhost', database='Agenda', port='3306')

#if conexao.is_connected():
    #print('Conectado com sucesso!')

url="https://renatagregorini.webnode.page/"
requisicao = requests.get(url)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.content, "html.parser")


titulo = site.find("title")
print(titulo)

gregorini = site.find("span", class_="sit-w")
print(gregorini.get_text())

assista = site.find('span', class_= "b-btn-t")
print(assista.get_text())

clipe = site.find_all("div", class_= "b-btn-c i-a") 
for links in clipe:
    link = links.find('a', href = True)
    comp = link['href']
    abs_url = f'{comp}'
    print(abs_url)

agenda = site.find("div" , class_="mt-c cf")
print(agenda.get_text())

