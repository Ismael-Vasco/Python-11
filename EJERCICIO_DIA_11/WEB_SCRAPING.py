import bs4
import requests     #busqueda
import re


resultado = requests.get("https://escueladirecta-blog.blogspot.com")

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#print(sopa.select('h1'))
#print(sopa.select('title')[0].getText())  #texto sin las etiquetas html

#print(sopa.select('p style'))

imagen = sopa.select('img')
print(imagen)

