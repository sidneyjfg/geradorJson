import xmltodict
import json
import os

# Obter o nome do único arquivo XML no diretório atual
arquivos_xml = os.listdir(".")
arquivo_xml = [arquivo for arquivo in arquivos_xml if arquivo.endswith(".xml")]

if len(arquivo_xml) != 1:
    print("Erro: Deve haver exatamente um arquivo XML no diretório.")
    exit()

arquivo_xml = arquivo_xml[0]

# Ler os dados do XML
with open(arquivo_xml, "rb") as f:
    xml_data = xmltodict.parse(f)

# Função para extrair dados do XML com tratamento de exceção para chaves ausentes
def extrair_dado(chaves, xml_data):
    try:
        dado = xml_data
        for chave in chaves.split('.'):
            if chave.startswith('@%'):
                dado = dado[chave[1:]]
            else:
                dado = dado[chave]
        return dado
    except KeyError:
        return None

def extrair_valor_apos_dois_pontos(dado):
    if dado:
        # Verifica se há ":" no dado
        if ":" in dado:
            # Encontra a posição do ":" e pega os 16 caracteres após ele
            index = dado.index(":") + 1
            return dado[index:index+16]
        else:
            return dado
    else:
        return None


def converter_formato_data(dado):
    if dado:
        # Verifica se há ":" no dado
        if "-" in dado:
            # Encontra a posição do ":" e pega os 16 caracteres após ele
            index = dado.index("-") + 2
            return dado[index:index+".323Z"]
        else:
            return dado
    else:
        return None

# Mapeamento dos dados
mapeamento_dados = {
    "idPedidoHub": extrair_valor_apos_dois_pontos(extrair_dado("nfeProc.NFe.infNFe.det.infAdProd", xml_data)),
    "idPedidoCanal": extrair_valor_apos_dois_pontos(extrair_dado("nfeProc.NFe.infNFe.det.infAdProd", xml_data)),
    "dataPedido": extrair_dado("nfeProc.NFe.infNFe.ide.dhEmi", xml_data)[:-6]+".323Z",
    "dataEntrega": extrair_dado("nfeProc.NFe.infNFe.ide.dhEmi", xml_data)[:-15],
    "idCanal": 2,
    "idLoja": "1",
    "idHub": 2,
    "observacoesEntrega": None,
    "status": 0,
    "entrega": {
        "cep": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.CEP", xml_data),
        "numero": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.nro", xml_data),
        "endereco": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.xLgr", xml_data),
        "complemento": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.xCpl", xml_data),
        "bairro": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.xBairro", xml_data),
        "cidade": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.xMun", xml_data),
        "estado": extrair_dado("nfeProc.NFe.infNFe.dest.enderDest.UF", xml_data)
    },
    "cliente": {
        "cnpjCpf": extrair_dado("nfeProc.NFe.infNFe.dest.CPF", xml_data),
        "ie": "",
        "rg": "",
        "nome": extrair_dado("nfeProc.NFe.infNFe.dest.xNome", xml_data),
        "ddd": "11",
        "telefone": None,
        "celular": "111111111",
        "email": extrair_valor_apos_dois_pontos(extrair_dado("nfeProc.NFe.infNFe.det.infAdProd", xml_data))+"@mercadolibre.com",
        "nomeFantasia": extrair_dado("dest.xNome", xml_data)
    },
    "pagamento": {
        "tipoPagamento": 2,
        "bandeira": 0,
        "valorDesconto": extrair_dado("nfeProc.NFe.infNFe.total.ICMSTot.vDesc", xml_data),
        "valorFrete": extrair_dado("nfeProc.NFe.infNFe.total.ICMSTot.vFrete", xml_data),
        "valorTotal": extrair_dado("nfeProc.NFe.infNFe.total.ICMSTot.vNF", xml_data),
        "parcelas": 1
    },
    "fulfillment": 1,
    "produtos": [
        {
            "sku": extrair_dado("nfeProc.NFe.infNFe.det.prod.cProd", xml_data),
            "quantidade": extrair_dado("nfeProc.NFe.infNFe.det.prod.qCom", xml_data),
            "precoUnitario": extrair_dado("nfeProc.NFe.infNFe.det.prod.vUnCom", xml_data)[:-6],
            "idPedidoCanal": extrair_valor_apos_dois_pontos(extrair_dado("nfeProc.NFe.infNFe.det.infAdProd", xml_data)),
            "valorComissao": 0
        }
    ]
}


pedido = extrair_valor_apos_dois_pontos(extrair_dado("nfeProc.NFe.infNFe.det.infAdProd", xml_data))
#print()
# Exibir os dados em formato JSON
with open(pedido, "w") as arquivo_json:
    json.dump(mapeamento_dados, arquivo_json, indent=4)

print(f"Arquivo JSON '{pedido}'.json criado com sucesso!")