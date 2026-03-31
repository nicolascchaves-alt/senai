#Imagine que você é um desenvolvedor encarregado de criar um sistema de controle de acesso para uma empresa de coworking. O sistema deve funcionar da seguinte maneira:
#Os membros têm acesso ilimitado durante o horário comercial (das 9h às 18h) de segunda a sexta-feira.
#Visitantes têm acesso limitado a um período máximo de 4 horas dentro do horário comercial.
#Durante o fim de semana (sábado e domingo), apenas os membros têm acesso ao espaço.
#Elabore um programa em Python que:
#A. Realize um print de boas-vindas que inclua o seu nome.
#B. Solicite ao usuário que insira se é um membro ou visitante e, se for um visitante, o tempo de permanência desejado em horas (valor inteiro).
#C. Calcule e retorne se o acesso é permitido ou não, com base nas regras mencionadas.
#D. Utilize estruturas condicionais (if, elif, else) para implementar as diferentes condições de acesso.
#E. Inclua comentários no código para explicar a lógica por trás de cada condição.
#F. Apresente uma mensagem na saída de console indicando se o acesso foi permitido ou não, e, se não foi permitido, informe o motivo.
#A. Print de boas-vindas
tipo_usuario = 0
tempo_permanencia = 0

print("Bem-vindo ao sistema de controle de acesso do Coworking Space!")
print("Desenvolvido por Murilo Bondan ")
tipo_usuario = input("Você é um membro ou visitante? (Digite 'membro' ou 'visitante'): ").strip().lower()  
#strip() é utilizado para remover os espaços em branco no início e no final da string, garantindo que a entrada do usuário seja processada corretamente mesmo que haja espaços extras.
#lower() é utilizado para converter a entrada do usuário para minúsculas, permitindo que o usuário digite 'Membro', 'MEMBRO', 'Visitante', 'VISITANTE' ou 'visitante' sem se preocupar com a caixa das letras, garantindo que a comparação seja feita de forma consistente.
if tipo_usuario == 'membro':
    for i in range(9,19):
        print(f"Bem-vindo, membro! Você tem acesso ilimitado durante o horário comercial. Horário atual: {i}h")
        print("Aproveite seu tempo no coworking!")
elif tipo_usuario == 'visitante':
    tempo_permanencia = int(input("Digite o tempo de permanência desejado em horas (valor inteiro): "))
    #int() é utilizado para converter a entrada do usuário, que é uma string, em um valor inteiro, permitindo que o programa possa comparar o tempo de permanência com o limite de 4 horas.
    if tempo_permanencia <= 4:
        print("Acesso permitido para visitante. Aproveite seu tempo no coworking!")
    else:
        print("Acesso negado para visitantes. O seu tempo de permanência excedeu o limite de tempo permitido (4 horas).")
else:
    print("Acesso negado. Por favor, insira 'membro' ou 'visitante' para identificar seu tipo de usuário.")
#else é utilizado para lidar com o caso em que o usuário insere um tipo de usuário inválido, garantindo que o programa responda de forma adequada e informe o motivo do acesso negado.