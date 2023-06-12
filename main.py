from nolinha import NoLinha
from nopalavra import NoPalavra


class OcorrenciadePalavras:
    def __init__(self):
        self.primeira_palavra = None
        self.primeira_tamanho = None
        self.ultima_palavra = None
        self.ultima_tamanho = None
        self.frases = []

    # buscar de palavras
    def consulta_palavra(self, palavra):
        no_atual = self.primeira_palavra
        while no_atual is not None:
            if no_atual.palavra == palavra:
                return no_atual
            no_atual = no_atual.proxPalavra

    # buscar tamanho
    def consultar_tamanho(self, tamanho):
        no_atual = self.primeira_tamanho
        while no_atual is not None:
            if no_atual.palavra == tamanho:
                return no_atual
            no_atual = no_atual.proxTamanho

    # inserir tamanho
    def insercao_tamanho(self, novo_no):
        tam_palavra = len(novo_no.palavra)
        novo_tam = NoPalavra(tam_palavra)
        novo_tam.proxTamanho = self.primeira_tamanho
        self.primeira_tamanho = novo_tam
        novo_tam.proxPalavra = novo_no

    # inserir as palavras
    def insercao_palavras(self, palavra, numero_linha):
        no_palavra = self.consulta_palavra(palavra)

        if no_palavra:
            no_linhas = no_palavra.linhas
            while no_linhas.prox_linha:
                no_linhas = no_linhas.prox_linha
            novo_no_linha = NoLinha(numero_linha)
            no_linhas.prox_linha = novo_no_linha
            no_palavra.ocorrs += 1
        else:
            novo_no_palavra = NoPalavra(palavra)
            novo_no_palavra.ocorrs = 1
            novo_no_palavra.linhas = NoLinha(numero_linha)

            if not self.primeira_palavra:
                self.primeira_palavra = novo_no_palavra
                self.ultima_palavra = novo_no_palavra
            else:
                self.ultima_palavra.proxPalavra = novo_no_palavra
                self.ultima_palavra = novo_no_palavra

            tam_palavra = len(palavra)
            no_tamanho = self.consultar_tamanho(tam_palavra)
            if no_tamanho:
                atual = no_tamanho
                while atual.proxTamanho and atual.proxTamanho:
                    atual = atual.proxTamanho
                novo_no_palavra.proxTamanho = atual.proxTamanho
                atual.proxTamanho = novo_no_palavra
            else:
                self.insercao_tamanho(novo_no_palavra)

    # lista linhas em que uma determinada palavra ocorre
    def listar_linhas(self, palavra):
        no_palavra = self.consulta_palavra(palavra)

        if no_palavra:
            linhas = []
            no_linhas = no_palavra.linhas
            while no_linhas:
                linhas.append(no_linhas.numero_linha)
                no_linhas = no_linhas.prox_linha
            print(*linhas)

    # lista palavras por número de letras
    """ """
    # lista palavras em ordemalfabética
    """"""

    # número de vezes em que uma palavra ocorre
    def contar_ocorrencias(self, palavra):
        no_palavra = self.consulta_palavra(palavra)
        ocorrencias = no_palavra.ocorrs if no_palavra else 0
        print(f"{palavra} {ocorrencias}")

    # listar todas as paalvras
    def listar_tudo(self):
        atual = self.primeira_palavra
        todas_palavras = []

        while atual:
            todas_palavras.append(atual.palavra)
            atual = atual.proxPalavra

        for palavra in sorted(todas_palavras):
            print(palavra)


def rodar_comandos():
    ocorrs = OcorrenciadePalavras()
    num_linhas = int(input())
    linhas = [input() for _ in range(num_linhas)]

    for i in range(num_linhas):
        linha = linhas[i]
        palavra = ""
        for char in linha:
            if char != " ":
                palavra += char
            else:
                if palavra != "":
                    ocorrs.insercao_palavras(palavra, i + 1)
                    palavra = ""
        if palavra != "":
            ocorrs.insercao_palavras(palavra, i + 1)

    while True:
        comando = input()
        if comando == "e":
            break

        if comando[0] == "l":
            palavra = input()
            ocorrs.listar_linhas(palavra)
        elif comando[0] == "n":
            palavra = input()
            ocorrs.contar_ocorrencias(palavra)
        elif comando[0] == "a":
            ocorrs.listar_tudo()


rodar_comandos()
