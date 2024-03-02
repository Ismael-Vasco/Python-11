import bs4
import requests

# url sin numero de pagina 
url_base = 'https://books.toscrape.com/catalogue/page-{}.html' # se agreagan llaves para que itere en todas las paginas

#for n in range(1,11):              # para iterar en todas las paginas de la url_base
    #print(url_base.format(n))

#llamar la url en la pagina 1
#resultado = requests.get(url_base.format(1))

# asignar a sopa 'resultado.text' para llerlo en html
#sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


# llamar al titulo del libro que aparece de primero en la pagina 1
#libros = sopa.select(".product_pod")

#ejemplo = libros[0].select("a")[1]['title']

#print(ejemplo)

#lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas

for pagina in range(1, 51):

    # crear soup en cada pagina
    url_pagina = url_base.format(pagina)

    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')


    # sleeccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for lib in libros:

        # chequear las estrellas (mayores o iguales a 4)
        if len(lib.select('.star-rating.Four')) != 0 or len(lib.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            titulo_libro = lib.select('a')[1]['title']

            #agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

# ver los libros de 4 y 5 estrellas

try:
    if len(titulos_rating_alto) > 0:
        count = 0
        print("\n" +"*"*5 +"Estos son los titulos de las peliculas que cumplen" + "*"*5 +"\n"
              + "*"*5+ "Cumplen con 4 & 5 estrellas para el scrapping"+ "*"*5 +"\n")
        for t in titulos_rating_alto:
            count += 1
            print(f'{count}: {t}')
            
except:
    print("Algo sucedio")

