
"""
Validacion de XML 
"""

import json
import xmltodict
import xml.etree.ElementTree as XML
from lxml import etree
from requests import request

"""Expresiones de URL"""
url_xml="./carta.xml"
url_xsd= "./carta.xsd"

"""Expresiones de XPATH"""
xpath = input('ingrese su ruta xpath ')
#xpath = '//remitente/nombre/text()'

"""Expresiones de JSON"""
json_ = input('desea transformar a json? Escribe y  ')
url_json= '//remitente/nombre/text()'

def validate(xml: str, xsd: str) -> bool:
    """Funcion validadora"""
    xmlschema_doc = etree.parse(xsd)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml)
    result = xmlschema.validate(xml_doc)
    Search(xml_doc)
    if(Json_validate(json_) ):
         
        tree = XML.parse(xml)
        xml_data = tree.getroot()
        xmlstr =  XML.tostring(xml_data, encoding='utf-8', method='xml')
        Json_transform(xml,xmlstr)

    return result

def Search(xml_doc: str) -> bool:
    """Funcion buscador XPATH"""
    xml_nombre= xml_doc.xpath(xpath)
    print(xml_nombre)
    return True

def Json_validate(json_ : str) -> bool:
    """Funcion validar existencia"""
    if (json_== 'y' or json_== 'Y' ):
        return True
    else:
        return False

def Json_transform(xml_doc : str, xmlstr : str) -> bool:
    """Condicional validacion json"""

    with open(xml_doc) as xml_file:

        data_dict = xmltodict.parse( xmlstr)
        xml_file.close()
        
        json_data = json.dumps(data_dict)
            
        with open("data.json", "w") as json_file:
            json_file.write(json_data)
            json_file.close()

"""Condicional validacion xml"""
if validate(url_xml,url_xsd):
    print(True)
else:
    print(False)

