import os
import xml.etree.ElementTree as ET
from django.http import HttpResponse
from django.conf import settings
from .models import Associado

def gerar_xml_associado(request, associado_id):
    # Busca o associado pelo ID
    associado = Associado.objects.get(id=associado_id)

    # Criação do XML
    root = ET.Element("Associado")
    ET.SubElement(root, "Nome").text = associado.nome
    ET.SubElement(root, "CPF").text = associado.cpf
    ET.SubElement(root, "Email").text = associado.email
    ET.SubElement(root, "Telefone").text = associado.telefone
    ET.SubElement(root, "Endereco").text = associado.endereco

    # Converter para XML
    tree = ET.ElementTree(root)

    # Caminho da pasta xml/
    pasta_xml = os.path.join(settings.BASE_DIR, "xml")
    nome_arquivo = f"associado_{associado.id}.xml"
    caminho_completo = os.path.join(pasta_xml, nome_arquivo)

    # Salvar o arquivo
    tree.write(caminho_completo, encoding="utf-8", xml_declaration=True)

    return HttpResponse(f"XML gerado com sucesso: {nome_arquivo}")
