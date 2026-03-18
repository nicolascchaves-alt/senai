estoque = {}
print("bem vindo ao sistema de gestão de estoque produzido por Nicolas Calozir")
while True:
    #while é utilizado para criar um loop infinito, permitindo que o usuário registre várias entradas e saídas de produtos até decidir sair do sistema.
    operacao = input ("deseja registrar a entrada e saída de produtos? (digite 'entrada ou saída') ou 'sair'").lower()
    #lower é utilizado para converter a string para minúscula, assim o sistema aceita tanto 'Entrada' quanto 'entrada' como entrada válida.
    if operacao == 'sair':
        break
    #break é utilizado para sair do loop quando o usuário digitar 'sair', encerrando o programa.
    if operacao not in ['entrada', 'saída','sair']:
        #not in é utilizado para verificar se a operação digitada pelo usuário é válida, ou seja, se é 'entrada', 'saída' ou 'sair'. Se a operação for inválida, o sistema exibe uma mensagem de erro e continua para a próxima iteração do loop, permitindo que o usuário corrija a entrada.
        print("operacao inavalida.")
        continue
    #continue é utilizado para pular o restante do código dentro do loop e iniciar a próxima iteração, permitindo que o usuário corrija a entrada inválida.
    produto = input("digite o nome do produto: ").strip()
    #strip é utilizado para remover espaços em branco no início e no final da string, garantindo que o nome do produto seja registrado corretamente.
    qtd = int(input("digite a quantidade: "))
    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
        #get é utilizado para remover a necessidade de verificar se o produto já existe no dicionário estoque, se ele não existir, ele retorna a 0.
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro: produto inexistente ou estoque insuficiente para retirar.")

print("\n ---estoque Final ---:")
for p, q in estoque.items():
    #for p, q in estoque.items() é utilizado para iterar sobre os itens do dicionário estoque, onde p representa o nome do produto e q representa a quantidade disponível. O método items() retorna uma lista de tuplas contendo os pares chave-valor do dicionário, permitindo que o loop acesse tanto o nome do produto quanto a quantidade correspondente para exibir o estoque final de forma clara e organizada.
    print(f"{p}: {q}") 
    #print é utilizado para exibir o nome do produto e a quantidade disponível no estoque final, utilizando uma f-string para formatar a saída de forma clara e legível.