import tkinter as tk
import requests
from bs4 import BeautifulSoup


def obtener_valor_dolar(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    dolar_element = soup.find("div", class_="sell-value")
    valor_dolar_str = dolar_element.text.strip().replace("$", "").replace(",", ".")
    valor_dolar = float(valor_dolar_str)
    return valor_dolar


def obtener_valor_mep(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    for td in soup.find_all('td', class_='name'):
        if 'DÓLAR MEP' in td.get_text():
            moneda = td.find_next_sibling('td', class_='sell').find(
                'div', class_='sell-value').get_text(strip=True)
            break
    valor_moneda_str = moneda.replace("$", "").replace(",", ".")
    valor_moneda = float(valor_moneda_str)
    #print(valor_moneda)
    return valor_moneda


def obtener_valor_may(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    for td in soup.find_all('td', class_='name'):
        if 'DÓLAR MAYORISTA' in td.get_text():
            monedaMAY = td.find_next_sibling('td', class_='sell').find(
                'div', class_='sell-value').get_text(strip=True)
            break
    valor_monedaMAY_str = monedaMAY.replace("$", "").replace(",", ".")
    valor_monedaMAY = float(valor_monedaMAY_str)
    #print(valor_monedaMAY)
    return valor_monedaMAY


def obtener_valor_tur(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    for td in soup.find_all('td', class_='name'):
        if 'DÓLAR TURISTA' in td.get_text():
            monedaTUR = td.find_next_sibling('td', class_='sell').find(
                'div', class_='sell-value').get_text(strip=True)
            break
    valor_monedaTUR_str = monedaTUR.replace("$", "").replace(",", ".")
    valor_monedaTUR = float(valor_monedaTUR_str)
    #print(valor_monedaTUR)
    return valor_monedaTUR


#Dólar MEP --------------------------------------------------------
def convertir_mep(cantidad, from_currency, to_currency):
    valorMoneda = obtener_valor_mep(
        "https://www.cronista.com/MercadosOnline/dolar.html")

    if from_currency == "ARS" and to_currency == "USD":
        cantidad_convertida = cantidad / valorMoneda
        return round(cantidad_convertida, 5)
    elif from_currency == "USD" and to_currency == "ARS":
        cantidad_convertida = cantidad * valorMoneda
        return round(cantidad_convertida, 2)
    elif from_currency == to_currency:
        return cantidad
    else:
        raise Exception("moneda inválida")


def dolar_mep():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_mep(cantidad, "ARS", "USD")
    etiqueta_resultado.config(text=resultado)


def peso():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_mep(cantidad, "USD", "ARS")
    etiqueta_resultado.config(text=resultado)


#Dólar OFICIAL -------------------------------------------------
def convertir_oficial(cantidad, from_currency, to_currency):
    valorMoneda = obtener_valor_dolar(
        "https://www.cronista.com/MercadosOnline/dolar.html")

    if from_currency == "ARS" and to_currency == "USD":
        cantidad_convertida = cantidad / valorMoneda
        return round(cantidad_convertida, 5)
    elif from_currency == "USD" and to_currency == "ARS":
        cantidad_convertida = cantidad * valorMoneda
        return round(cantidad_convertida, 2)
    elif from_currency == to_currency:
        return cantidad
    else:
        raise Exception("moneda inválida")


def dolar_oficial():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_oficial(cantidad, "ARS", "USD")
    etiqueta_resultado.config(text=resultado)


def peso_oficial():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_oficial(cantidad, "USD", "ARS")
    etiqueta_resultado.config(text=resultado)

#Dólar MAYORISTA -------------------------------------------------
def convertir_may(cantidad, from_currency, to_currency):
    valorMoneda = obtener_valor_may(
        "https://www.cronista.com/MercadosOnline/dolar.html")

    if from_currency == "ARS" and to_currency == "USD":
        cantidad_convertida = cantidad / valorMoneda
        return round(cantidad_convertida, 5)
    elif from_currency == "USD" and to_currency == "ARS":
        cantidad_convertida = cantidad * valorMoneda
        return round(cantidad_convertida, 2)
    elif from_currency == to_currency:
        return cantidad
    else:
        raise Exception("moneda inválida")


def dolar_may():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_may(cantidad, "ARS", "USD")
    etiqueta_resultado.config(text=resultado)


def peso_may():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_may(cantidad, "USD", "ARS")
    etiqueta_resultado.config(text=resultado)


#Dólar TURISTA -------------------------------------------------
def convertir_tur(cantidad, from_currency, to_currency):
    valorMoneda = obtener_valor_tur(
        "https://www.cronista.com/MercadosOnline/dolar.html")

    if from_currency == "ARS" and to_currency == "USD":
        cantidad_convertida = cantidad / valorMoneda
        return round(cantidad_convertida, 5)
    elif from_currency == "USD" and to_currency == "ARS":
        cantidad_convertida = cantidad * valorMoneda
        return round(cantidad_convertida, 2)
    elif from_currency == to_currency:
        return cantidad
    else:
        raise Exception("moneda inválida")


def dolar_tur():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_tur(cantidad, "ARS", "USD")
    etiqueta_resultado.config(text=resultado)


def peso_tur():
    cantidad = float(entrada_cantidad.get())
    resultado = convertir_tur(cantidad, "USD", "ARS")
    etiqueta_resultado.config(text=resultado)


#APP TKINTER-------------------------------------------------------
ventana = tk.Tk()
ventana.title("Conversor de Moneda")

marco = tk.LabelFrame()
marco.place(x=20, y=20, width=690, height=460)
marco.configure(background='azure')

ventana.geometry('730x500')
ventana.configure(background='DodgerBlue4')

etiqueta_intro = tk.Label(ventana, text="Ingrese el monto que quiere consultar\n y seleccione la opción a la que desea convertir", font='Bahnschrift', background='azure')
etiqueta_intro.place(x=100, y=40)

etiqueta_cantidad = tk.Label(ventana, text="Cantidad", font='Bahnschrift', background='azure')
etiqueta_cantidad.place(x=100, y=100)


entrada_cantidad = tk.Entry(ventana, font='Bahnschrift')
entrada_cantidad.place(x=175, y=105, width=160, height=20)



dolares_mep = tk.Button(ventana, text="Peso a Dolar MEP", command=dolar_mep, font='Bahnschrift', background='white')
dolares_mep.place(x=170, y=230, width=160, height=50)

pesos = tk.Button(ventana, text="Dolar MEP a Peso", command=peso, font='Bahnschrift', background='white')
pesos.place(x=400, y=230, width=160, height=50)

dolares_oficial = tk.Button(ventana, text="Peso a Dolar Oficial", command=dolar_oficial, font='Bahnschrift', background='white')
dolares_oficial.place(x=170, y=170, width=160, height=50)

pesos_oficial = tk.Button(ventana, text="Dolar Oficial a Peso", command=peso_oficial, font='Bahnschrift', background='white')
pesos_oficial.place(x=400, y=170, width=160, height=50)

dolares_may = tk.Button(ventana, text="Peso a Dolar MAY", command=dolar_may, font='Bahnschrift', background='white')
dolares_may.place(x=170, y=290, width=160, height=50)

pesos_may = tk.Button(ventana, text="Dolar MAY a Peso", command=peso_may, font='Bahnschrift', background='white')
pesos_may.place(x=400, y=290, width=160, height=50)

dolares_tur = tk.Button(ventana, text="Peso a Dolar TUR", command=dolar_tur, font='Bahnschrift', background='white')
dolares_tur.place(x=170, y=350, width=160, height=50)

pesos_tur = tk.Button(ventana, text="Dolar TUR a Peso", command=peso_tur, font='Bahnschrift', background='white')
pesos_tur.place(x=400, y=350, width=160, height=50)

igual = tk.Label(ventana, text="=", font='Bahnschrift', background='azure')
igual.place(x=310, y=100)

etiqueta_resultado = tk.Label(ventana, text="Cantidad Convertida", font='Bahnschrift', background='azure')
etiqueta_resultado.place(x=320, y=100)

ventana.mainloop()
