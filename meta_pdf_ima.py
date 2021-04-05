from tkinter.filedialog import askopenfilename

from PIL import Image
from PIL.ExifTags import TAGS
from PyPDF2 import PdfFileReader

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANALIZANDO LOS METADATOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def obtenerMetadatos():
    print("Escoja su archivo PDF")
    archivo_pdf = PdfFileReader(askopenfilename())

    info_documento = archivo_pdf.getDocumentInfo()

    print("\n")
    print("###############################################################################")
    print("                         Información metadatos")
    print("###############################################################################")
    print("\n")

    for metadato in info_documento:
        print("[+] " + metadato + ":" + info_documento[metadato])


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                            ANALIZANDO LOS METADATOS

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def analisis_imagen():

    metadatos_exif = {}

    archivo_imagen = Image.open(askopenfilename())

    info = archivo_imagen._getexif()

    print("\n")
    print("###############################################################################")
    print("                         Información general")
    print("###############################################################################")
    print("\n")
    print(info)

    if (info):
        for (tag,value) in info.items():
            decoded = TAGS.get(tag,tag)
            metadatos_exif[decoded] = value

        if metadatos_exif:

            print("\n")
            print("###############################################################################")
            print("                         Información metadatos")
            print("###############################################################################")
            print("\n")

            for meta_info in metadatos_exif:
                print("[+] " + str(archivo_imagen) + " Datos: " + str(metadatos_exif[meta_info]))






