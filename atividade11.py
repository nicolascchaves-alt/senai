soma = 0
produto = " "
retirar_produto = True
quantidade = 0
opcao = " "
adicionar_produto = False
print("boas-vindas, digite seu nome: ")
nome = input()
print(f"ola {nome} seja bem-vindo ao sistema de estoque")
print("deseja retirar ou adicionar um produto ao estoque? (retirar/adicionar)")
opcao = input()
if opcao == "retirar":
    retirar_produto = True
elif opcao == "adicionar":
    retirar_produto = False
if retirar_produto:
    print("digite o nome do produto a ser retirado: ")
    produto = input()
    print(f"quantidade de {produto} a ser retirada: ")
    quantidade = int(input())
    print(f"retirando {quantidade} de {produto}")
else:
    print("digite o nome do produto a ser adicionado: ")
    produto = input()
    print(f"quantidade de {produto} a ser adicionada: ")
    quantidade = int(input())
    print(f"adicionando {quantidade} de {produto}")
    print("deseja retirar ou adicionar outro produto ao estoque? (retirar/adicionar)")
opcao = input()
if opcao == "sim":
    adicionar_produto = True
else:
    adicionar_produto = False
    while adicionar_produto:
        print("digite o nome do produto a ser adicionado: ")
        produto = input()
        print(f"quantidade de {produto} a ser adicionada: ")
        quantidade = int(input())
        print(f"adicionando {quantidade} de {produto}")
        print("deseja retirar ou adicionar outro produto ao estoque? (retirar/adicionar)")
        opcao = input()
        if opcao == "sim":
            adicionar_produto = True
        else:
            adicionar_produto = False   