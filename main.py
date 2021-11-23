from manipulacao_arquivos import Manipula_arquivo
import os.path

def  main():
    op = 0 
    file = Manipula_arquivo() #Instancia um objeto da classe Manipula_arquivo

    while True: #Menu de opções
        op = int(input("Opções:\n"
                        "1 - Criar arquivo.\n"
                        "2 - Incluir registros.\n"
                        "3 - Mostrar Dados e pesquisar ID.\n"
                        "4 - Sair.\n"
                        "Informe opção:"))

        if op == 1:
            nome = input("Digite o nome que deseja dar ao seu arquivo .csv:")
            file.cria_arquivo(nome) #Cria um arquivo csv e ou verifica se já existe um arquivo com o mesmo nome.

        elif op == 2:
            try:
                if os.path.isfile(nome + '.csv'):#Verifica se existe um arquivo csv
                    file.inserir_dados()# Chama a API e pega n dados
                    print("Dados Inseridos \n")
            except UnboundLocalError:
                print("\nARQUIVO AINDA NÃO CRIADO OU NÃO DEFINIDO O NOME DO ARQUIVO \n")

        elif op == 3:
            try:
                if os.path.isfile(nome + '.csv'):
                    file.print_dados() #Mostra todos os dados do arquivo csv

                    while True:# Menu de opções
                        op1 = int(input("Opções:\n"
                                        "1 - Busca Sequencial.\n"
                                        "2 - Busca Binaria.\n"
                                        "3 - Sair.\n"
                                        "Informe opção:"))

                        if op1 == 1:
                            valor_buscado = int(input("Informe valor para buscar:"))
                            resposta = file.busca_sequencial(valor_buscado)# Busca um valor utilizando busca sequencial 
                            
                            if resposta < 0:
                                print("\nValor", valor_buscado,"não encontrado na lista.\n")
                            else:
                                print("Valor", valor_buscado,"encontrado na posição", resposta, "da lista.")
                                print(f"Foram feitas {resposta} iterações\n") #Mostra a quantidade de iterações

                        elif op1 == 2:
                            valor_buscado = int(input("Informe valor para buscar:"))
                            resposta = file.busca_binaria(valor_buscado)# Busca um valor utilizando busca binaria
                            
                            if resposta < 0:
                                print("\nValor", valor_buscado,"não encontrado na lista.\n")
                            else:
                                print("Valor", valor_buscado,"encontrado na posição", resposta, "da lista.")
                                print(f"Foram feitas {resposta} iterações\n") #Mostra a quantidade de iterações

                        elif op1 == 3:
                            break

                        else:
                            print("Opção inválida.")

            except UnboundLocalError:
                print("\nARQUIVO AINDA NÃO CRIADO OU NÃO DEFINIDO O NOME DO ARQUIVO \n")

        elif op == 4:
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()