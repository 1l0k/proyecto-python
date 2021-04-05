##########################################################

print("Script completo de busqueda")

##########################################################
import shodan
import whois11
import pprintpp
import dns
import dns.resolver
from termcolor import colored
import pygeoip
from meta_pdf_ima import obtenerMetadatos, analisis_imagen
###########################################################################################################
###########################################################################################################

"""""""""""""""""""""""""""""""""""""""""
            Script de shodan 

"""""""""""""""""""""""""""""""""""""""""
def busque_shodan():
    # Cambiar por su clave API de SHODAN
    ShodanKeyString = '' # <-------- poner entre las comillas su clave API

    # Realizamos la conexion con la base de datos de Shodan
    ShodanApi = shodan.Shodan(ShodanKeyString)

    try:
        # Buscamos en Shodan con el método WebAPI.search()
        resultados = ShodanApi.search(input("Que desea buscar: "))

        # Mostramos el resultado
        pprintpp.pprint('Cantidad de resultados encontrados: %s' % resultados['total'])

        for i in resultados['matches']:
            pprintpp.pprint('IP: %s' % i['ip_str'])
            pprintpp.pprint('Data: %s' % i['data'])
            pprintpp.pprint('Hostnames: %s' % i['hostnames'])
            pprintpp.pprint('Puerto: %s' % i['port'])
            pprintpp.pprint('')

    except shodan.APIError as e:

        pprintpp.pprint('Ups! Ha ocurrido un error: %s' % e)


    ######################################################################################################
    ######################################################################################################


"""""""""""""""""""""""""""""""""""""""""
            Script de whois11 

"""""""""""""""""""""""""""""""""""""""""
def busque_whois():
    pprintpp.pprint("")
    pprintpp.pprint("")
    pprintpp.pprint("Busqueda de whois")
    pprintpp.pprint("")
    pprintpp.pprint("empezando segundo script......")
    pprintpp.pprint("")
    pprintpp.pprint(whois11.whois(input("Escriba el sitio que desea buscar: ")))
    pprintpp.pprint("")
    pprintpp.pprint("")

    ##########################################################################################
    ##########################################################################################

def busque_dns():
    pprintpp.pprint("Ahora comienza el script para busqueda dns")
    pprintpp.pprint("Empezando tercer script.....")

    """""""""""""""""""""""""""""""""""""""""
            Script de dns 

    """""""""""""""""""""""""""""""""""""""""
    consul = input("Escriba el sitio que desea buscar: ")
    """Consulta sobre registro IPV4"""
    ansA = dns.resolver.query(consul,'A')

    """Consulta sobre registro IPV6"""
    ansAAAA = dns.resolver.query(consul,'AAAA')

    """Consulta sobre registro MailServers"""
    ansMX = dns.resolver.query(consul,'MX')

    """Consulta sobre registro NameServers"""
    ansNS = dns.resolver.query(consul,'NS')


    print (colored("\nRespuesta de DNS en IPV4: ",'red',attrs=['bold', 'blink']))
    print (ansA.response.to_text())

    print (colored("\nRespuesta de DNS en IPV6: ",'red', attrs=['bold', 'blink']))
    print (ansAAAA.response.to_text())

    print (colored("\nRespuesta de DNS en MailServers: ",'red',attrs=['bold', 'blink']))
    print (ansMX.response.to_text())

    print (colored("\nRespuesta de DNS en NameServers: ",'red',attrs=['bold', 'blink']))
    print (ansNS.response.to_text())

    ###############################################
    ###############################################

def busque_geoip():
    pprintpp.pprint("")
    pprintpp.pprint("")
    pprintpp.pprint("Busqueda de geoip")
    pprintpp.pprint("")
    pprintpp.pprint("empezando cuarto script......")
    pprintpp.pprint("")
    pprintpp.pprint("")
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                        scripts de goeip_info

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    gi = pygeoip.GeoIP('GeoLiteCity.dat')
    consul_name = input("Escriba el codigo por nombre EJEMPLO(hola.com): ")
    consul_address = input("Escriba el codigo por dirrecion EJEMPLO(192.168.168.161): ")
    pprintpp.pprint(colored("\n Código del pais del servidor por dominio: ",'red',attrs=['bold', 'blink']) + gi.country_code_by_name(consul_name))
    pprintpp.pprint(colored("\n Código del país del servidor por IP: ",'red',attrs=['bold', 'blink']) + gi.country_code_by_addr(consul_address))
    pprintpp.pprint(colored("\n Time zone del servidor por IP: ",'red',attrs=['bold', 'blink']) + gi.time_zone_by_addr(consul_address))

    pprintpp.pprint(colored("\n Información completa del servidor por IP: ",'red',attrs=['bold', 'blink']))

    pprintpp.pprint(gi.record_by_addr(consul_address))

    ######################################################################################################################
    ######################################################################################################################

def busque_pdf():
    obtenerMetadatos()

def busque_imag():
    analisis_imagen()
