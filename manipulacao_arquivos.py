import os.path
from numpy import savetxt
from pokeApi import PokemonAPI
from random import randint
import csv
import re

class Manipula_arquivo():

    __arquivo = None
    __lista_pokemons = None
    __lista_csv = None

    def __init__(self):
        self.__lista_pokemons = [] #Lista de pokemons
        self.__lista_csv = [] #Lista importada do arquivo csv

    def cria_arquivo(self,nome):#Esse metodo verifica se existe um arquivo csv, se não existir um arquivo é criado.
        if not os.path.isfile(nome + '.csv'):
            arquivo = open(nome + ".csv",'a')
            arquivo.close()
            self.__arquivo = nome + ".csv"
            print("Arquivo criado\n")
        else:
            self.__arquivo = nome + ".csv"
            print("Este arquivo ja existe\n")

    def inserir_dados(self):
        valor = int(input("Digite quantos registros você deseja inserir no seu .csv:"))
        lista_controle = []# Lista auxiliar 

        if valor <= 800:# Numero maximo de pokemons
            Objeto = PokemonAPI()# Instancia um objeto da classe PokemonAPI

            while len(lista_controle) < valor:#Faz enquanto a lista não estiver completa 
                num = randint(1,800)# Randomiza um numero para ser utilizado na API
                pokemon = Objeto.pega_informações(Objeto.pokeAPI(num))#Pega as informações do pokemon e guarda em uma variavel

                if pokemon not in self.__lista_pokemons:# Verifica se o pokemon não está na lista e o adiciona.
                    lista_controle.append(pokemon)

            self.__lista_pokemons.extend(lista_controle)#Concatena as listas
            savetxt(self.__arquivo, self.__lista_pokemons, delimiter =",",fmt ='% s')#Salva a lista no arquivo csv
        else:
            print('Não é possivel inserir mais de 800 dados')

    def print_dados(self):
        with open (self.__arquivo, "r") as f:#Abre o arquivo com with para garantir que ele seja fechado ao final da execução do metodo.
            dados = csv.reader(f, delimiter=",") #Abre o arquivo em modo leitura 
            self.__lista_csv = list(dados)# Trasnforma o arquivo csv em uma lista
            print("['ID', 'NOME', 'HABILIDADE']")
            for pokemon in self.__lista_csv:# Printa a lista
                print(pokemon)
            print("\n")
    
    def busca_sequencial(self, valor_buscado):# Busca um valor em uma lista utilizando busca sequencial
        resposta = -1
        i = 0
        while i < len(self.__lista_csv):
            linha = str(self.__lista_csv[i])
            linha = linha.split(",")
            if linha[0] == f"['{valor_buscado}'":
                resposta = i + 1
                print("\n['ID', 'NOME', 'HABILIDADE']") 
                print(self.__lista_csv[i])
            i+=1
        return resposta
    
    def gnome_sort(self):#O algoritmo percorre o vetor comparando seus elementos dois a dois, assim que ele encontra um elemento que está na posição incorreta, ou seja, 
        #um número maior antes de um menor, ele troca a posição dos elementos, e volta com este elemento até que encontre o seu respectivo lugar.
        indice = 0
        while indice < len(self.__lista_csv):

            if indice == 0:
                indice = indice + 1

            linha = str(self.__lista_csv[indice])
            linha = linha.split(",")
            linha = int(re.sub("\'|\[","",str(linha[0])))

            linha2 = str(self.__lista_csv[indice-1])
            linha2 = linha2.split(",")
            linha2 = int(re.sub("\'|\[","",str(linha2[0])))

            if linha >= linha2:
                indice = indice + 1

            else:
                self.__lista_csv[indice], self.__lista_csv[indice-1] = self.__lista_csv[indice-1], self.__lista_csv[indice]
                indice = indice - 1

    def busca_binaria(self, valor_buscado):# Ordena a lista utilizando gnome sort e depois procura um valor utilizando busca binaria
        self.gnome_sort()

        esquerda = 0
        direita = len(self.__lista_csv) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            linha = str(self.__lista_csv[meio])
            linha = linha.split(",")
            if linha[0] == f"['{valor_buscado}'":
                print("\n['ID', 'NOME', 'HABILIDADE']") 
                print(self.__lista_csv[meio])
                return meio + 1 
            elif linha[0] > f"['{valor_buscado}'":
                direita = meio - 1
            else:
                esquerda = meio + 1
        return -1