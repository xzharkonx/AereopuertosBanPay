from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from googleapiclient.discovery import build
from google.oauth2 import service_account
from django.core import serializers
import requests
import json
from .aereopuerto import Aereopuerto

import os

# Create your views here.

def home(request):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    DIRNAME = os.path.dirname(__file__)

    SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'private_key.json')

    print(SERVICE_ACCOUNT_FILE)

    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1G5darnYfuJvfPvaGZR9Y3cItm3wMbCQQ5DpZDkB7GQ0'

    # Range data.
    SAMPLE_RANGE_NAME = 'Hoja 1!A1:L7699'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L10'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L70'

    # Call service.
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API.
    try:
        
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    except Exception as e:
        print( type(e).__name__ )
        print("Ha ocurrido un error inesperado:",e)
        print("Vuelve a intentarlo nuevamente")

    values = result.get('values', [])

    if not values:
        print('No hay datos.')
    else:
        # Quitamos los titulos.
        values = values[1:]
        print("Total de Elementos",len(values)) # 7699
        print("Elementos de una fila",len(values[0]))
        return render(request, "core/index.html", {'aereopuertos':values})
    # return render(request, "core/index.html")

def aereopuertosAsia(request):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    DIRNAME = os.path.dirname(__file__)

    SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'private_key.json')

    print(SERVICE_ACCOUNT_FILE)

    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1G5darnYfuJvfPvaGZR9Y3cItm3wMbCQQ5DpZDkB7GQ0'

    # Range data.
    SAMPLE_RANGE_NAME = 'Hoja 1!A1:L7699'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L10'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L70'

    # Call service.
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API.
    try:
        
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    except Exception as e:
        print( type(e).__name__ )
        print("Ha ocurrido un error inesperado:",e)
        print("Vuelve a intentarlo nuevamente")

    values = result.get('values', [])

    if not values:
        print('No hay datos.')
    
    # Cabecera de datos.
    headData = values[0]
    # print(headData)

    # Datos.
    dataSheet = values[1:]
    # print(len(dataSheet[0])) # 12 Columnas

    listaAereopuertos = []

    # Ejemplo:
    # a = Aereopuerto(9310,"Daocheng Yading Airport","Daocheng","China","DCY","ZUDC",29.323056,100.053333,14472,8,"N","Asia/Shanghai")

    # Añadiendo los datos a los Objetos y agregandolos a la lista "listaAereopuertos"
    if not dataSheet:
        print('No hay datos.')
    else:
        for obj in range(0,len(dataSheet)):
            
    #         Mostando datos
    #         print(dataSheet[obj][0], dataSheet[obj][1], dataSheet[obj][2], dataSheet[obj][3], dataSheet[obj][4],
    #              dataSheet[obj][5], dataSheet[obj][6], dataSheet[obj][7], dataSheet[obj][8], dataSheet[obj][9],
    #              dataSheet[obj][10], dataSheet[obj][11])

            listaAereopuertos.append(Aereopuerto(dataSheet[obj][0], dataSheet[obj][1], dataSheet[obj][2], 
                dataSheet[obj][3], dataSheet[obj][4],dataSheet[obj][5], dataSheet[obj][6], dataSheet[obj][7],
                dataSheet[obj][8], dataSheet[obj][9], dataSheet[obj][10], dataSheet[obj][11]))


    # Ahora ya tendríamos una lista de Objetos de Aereopuertos con sus respectivos datos.
    # print("Mostrando los aereopuertos")
    # print("Total inicial de aereopuertos",len(listaAereopuertos),"\n")
    # for l in listaAereopuertos:
    #     print(l,"\n")
        

    print("Total de aereopuertos",len(listaAereopuertos))
    print("Aereopuertos",len(listaAereopuertos[0]))




    # Aereopuertos de Asia
    asiaAirport = []
    matrizDatos = []
    def getAirport(aereopuerto,paisesAsiaFiltrados):
        
        for p in range(0,len(paisesAsiaFiltrados)):
        
            # Para listas
            # print(paises[p]['name'], paises[p]['alpha2Code'] )
            # print(aereopuerto.getCountry(), aereopuerto.getAirportName())
            
            if aereopuerto.getCountry() == paisesAsiaFiltrados[p]['name']:

                aereopuerto.setNativeName(paisesAsiaFiltrados[p]['nativeName'])
                return aereopuerto

    # Para un solo pais
    # Nos retorna un tipo de dato byte y convertiremos a Diccionario
    # url = 'https://restcountries.eu/rest/v2/alpha/jp'

    # Para todos los paises
    # Nos retorna un tipo de dato byte y convertiremos a Lista
    url = 'https://restcountries.eu/rest/v2/all' # Lista

    # Obtenemos los datos
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
    else:
        print("Algo falló")


    # La cadena que nos retorna esta en bytes, la convertimos a str
    paisesDecodificados = content.decode("utf-8")


    paises = json.loads(paisesDecodificados)

    # Filtrar los paises de Asia.
    for l in paises:
        paisesAsiaFiltrados = list(filter(lambda p: p['region'] == 'Asia', paises))


    print("\nTotal de Aereopuertos",len(listaAereopuertos),"\n")


    for a in listaAereopuertos:
            
            # Retorna el aereopuerto de Asia
            aF=getAirport(a,paisesAsiaFiltrados)
            
            if aF: 
                asiaAirport.append(aF)


    print(len(asiaAirport))
    print(len(asiaAirport[0]))
    return render(request, "core/aereopuertosAsia.html", {'aereopuertos':asiaAirport})
    

def getAereopuertosRest(request):
    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    DIRNAME = os.path.dirname(__file__)

    SERVICE_ACCOUNT_FILE = os.path.join(DIRNAME, 'private_key.json')

    print(SERVICE_ACCOUNT_FILE)

    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)


    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1G5darnYfuJvfPvaGZR9Y3cItm3wMbCQQ5DpZDkB7GQ0'

    # Range data.
    SAMPLE_RANGE_NAME = 'Hoja 1!A1:L7699'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L10'
    # SAMPLE_RANGE_NAME = 'Hoja 1!A1:L70'

    # Call service.
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API.
    try:
        
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()

    except Exception as e:
        print( type(e).__name__ )
        print("Ha ocurrido un error inesperado:",e)
        print("Vuelve a intentarlo nuevamente")

    values = result.get('values', [])

    if not values:
        print('No hay datos.')
    else:
        return JsonResponse(values, safe=False)
