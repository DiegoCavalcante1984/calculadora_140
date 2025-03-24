import csv # biblioteca que sabe ler e escrever um arquivo csv

def ler_csv(arquivo_csv):
    dados_csv = []    # cria uma lista em branco
    try:#tentar tratanento de erro
        with open(arquivo_csv, newline="") as massa:#new line signifiica final de linha
            tabela = csv.reader(massa, delimiter=",")#com os dado do arquivo,menos o cabeçalho
            next(tabela)#pula linha de cabeçalho 
            for linha in tabela:                #para cada linha em tabela                                       #informando que o separador é a virgula   
                dados_csv.append(linha) 
        return dados_csv 
    except FileNotFoundError:
        print(f'Arquivo não encontrado:{arquivo_csv}')#mensagem de erro de arquivo não encontrado
    except Exception as fail:#Qualquer erro não previsto
        print(f'Falha imprevista: {fail}')           