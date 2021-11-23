import requests

class PokemonAPI():# Class criada para utilizar a PokéAPI V2
    __id = None
    __nome = None
    __habilidade = None
    __api = None
    __request = None
    __poke = None

    def pokeAPI(self, pokemon):
        self.__api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}' #URL da API 
        self.__request = requests.get(self.__api)# Faz um pedido para a API
        self.__poke = self.__request.json()# Guarda o pedido em formato json em uma variavel
        return self.__poke

    def pega_informações(self, poke):# Deve ser informado uma variavel contendo o json
        self.__nome = poke['name']#Pega o nome do pokemon
        self.__id = poke['id']#Pega o ID do pokemon 
        self.__habilidade = poke['abilities'][0]['ability']['name']#Pega a primeira habilidade do pokemon
        linha_csv = (f"{self.__id}"+','+f"{self.__nome}"+','+f"{self.__habilidade}")# Concatena todos os dados em uma string 
        return linha_csv