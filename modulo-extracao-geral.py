import time

import requests

orgaos = [("ADAF", 158),("ADS", 117),("APOSENTADOS_EXECUTIVO", 31),("APOSENTADOS_ALEAM", 70),("APOSENTADOS_PGJ", 312),("APOSENTADOS_TCE", 342),("TJA", 303),("ARSEPAM", 115),("CASA_CIVIL_DO_GOVERNO", 159),("CASA_MILITAR", 94),("CB_CIVIS", 113),("CBMAM", 91),("CETAM", 150),("CGE", 154),("CSC", 111),("DETRAN", 63),("ERGSP", 27),("FAPEAM", 95),("FCECON", 34),("FEH", 1111111111),("FEI", 171),("FHAJ", 122),("FHEMOAM", 37),("FMT_AM", 86),("FUHAM", 32),("FUNDACAO_AMAZONPREV", 233),("FUNDACAO_VILA_OLIMPICA", 22222222),("FUNTEC", 93),("FVS", 124),("IDAM", 43),("JUCEA", 74),("OUVIDORIA_GERAL", 333333333),("PENSIONISTAS_EXECUTIVO", 231),("PENSIONISTAS_ALEAM", 231070),("PENSIONISTAS_PGJ", 373),("PENSIONISTAS_TCE", 358),("PENSIONISTAS_TJA", 306),("PGE", 163),("PM_ATIVOS", 88),("PM_CIVIS", 85),("POLICIA_CIVIL", 23),("PROCON", 168),
    ("PRODAM", 600), #TODO descomentar e tratar esse problema da PRODAM
    ("SEAD", 13),("SEAD_PENSAO_ESPECIA_I", 501),("SEAD_PENSAO_ESPECIA_II", 503),("IPAAM", 73),("IPEM_AM", 39),("SEAD_PENSAO_HANSENIANOS", 502),("SEAP", 128),("SEAS", 60),("SEC", 44),("SECOM", 126),("SECT", 61),("SEDECTI", 10),("SEDEL", 234),("SEDUC", 25),("SEFAZ", 7),("SEIND", 44444444),("SEINFRA", 59),("SEJEL", 55555555),("SEJUSC", 8),("SEMA", 65),("SEPED", 66666666),("SEPROR", 66),("SERFI", 170),("SERGB", 77777777),("SES", 2),("SETRAB", 88888888),("SGVG", 161),("SNPH", 118),("SRMM", 9999999),("SSP", 45),("SUHAB", 96),("UEA", 120),("UGPE", 121)
]

# Esse arquivo ele realiza o download de todos os arquivos referentes a salários de servidores CSV de todos os órgãos públicos do estado do amazonas

# Pasta de destino para os arquivos
pasta_destino = "C:/dev/a-tcc-2024/modulo-extracao/dados"
ano = 2018
for orgao in orgaos:
    ida = 1
    while ida <=12:
        if ida < 10: mes = f"0{ida}"
        else: mes = ida

        nome_arquivo = f"{orgao[1]}_{ano}{mes}"
        try:
            time.sleep(2)
            url = f"https://www.transparencia.am.gov.br/arquivos/{ano}/{nome_arquivo}.csv"
            response = requests.get(url)

            # Verifique se a solicitação foi bem-sucedida (status code 200)
            if response.status_code == 200:
                # Nome do arquivo com base no nome do órgão e data

                # Caminho completo do arquivo
                caminho_arquivo = pasta_destino + rf"\{nome_arquivo}.csv"

                with open(caminho_arquivo, "wb") as arquivo:
                    arquivo.write(response.content)
                # print(f"O arquivo {nome_arquivo} foi baixado com sucesso.")
            else:
                print(f"Não foi possível baixar o arquivo. Status code: {response.status_code} // Arquivo: {orgao[1]}")

        except Exception as e:
            print(f"Ocorreu um erro no arquivo {nome_arquivo} -- Erro: {e}")
        ida+=1