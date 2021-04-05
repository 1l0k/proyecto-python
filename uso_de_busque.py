import sys
from busqueda_completa import busque_shodan, busque_dns, busque_geoip, busque_whois, busque_pdf, busque_imag
print("\n#######################################################################################"
      "\n                               BUSQUEDA COMPLETA "
      "\n           AQUI SE ENCONTRARAN CON VARIAS HERRAMIENTAS DE RECOLLECION DE INFORMACION"
      "\n           AQUI SE PODRAN VER LAS OPCIONES A ELEGIR "
      "\n           1) BUSQUEDA POR SHODAN "
      "\n           2) BUSQUEDA DE DNS"
      "\n           3) BUSQUEDA GEOIP"
      "\n           4) BUSCAR METADATOS EN ARCHIVOS PDF"
      "\n           5) BUSCAR METADATOS EN IMAGENES"
      "\n#######################################################################################")

pregu = input("Escriba su opcion: ")

if pregu == "1":
    busque_shodan()
elif pregu == "2":
    busque_dns()
elif pregu == "3":
    busque_geoip()
elif pregu == "4":
    busque_whois()
elif pregu == "5":
    busque_pdf()
elif pregu == "6":
    busque_imag()
elif pregu >= "7":
    print("Escriba una opcion valida")
    sys.exit()
