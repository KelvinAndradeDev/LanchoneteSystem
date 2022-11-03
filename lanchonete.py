import time

def main():
    lanches = [('Big Burguer', 15), ('The crazy cheddar', 20),
               ('Morto de Fome', 25), ('Morte Subita', 30)]
    comprovante = ' '
    pedido = ''
    nome = take_name()
    endereco = take_adress(nome)
    mostrar_lanches(lanches)
    comprar_lanches(lanches,comprovante,pedido, nome, endereco)

# Tela inicial para pegar informacoes pessoas e dizer bem vindo
def take_name():
    print('==============================')
    print('Bem-Vindo ao GoodFood Delivery')
    print('==============================')
    print('Gostariamos de lhe conhecer melhor, qual seu o nome ?')
    nome = input()
    return nome
    # time.sleep(1)

def take_adress(nome):
    print(f'Muito bem {nome}, agora poderia nos dizer seu endereco ? ')
    endereco = input()
    print(f'Agora ja temos seu endereco de entrega {nome}, vamos ao pedido.')
    print('==============================')
    print('Carregando menu')
    return endereco


# A definicao mostrar lanches fara o cardapio, pegando por ordem os valores importados da lista lanches e enumerando de acordo com a posicao
def mostrar_lanches(lanches):
    print('==============================')
    for i, j in enumerate(lanches):
        print(f'{i} {j[0]} R$ {j[1]},00')

# A definicao comprar_lanches definira o lanche escolhido e a quantidade, ele ira calcular tambem o valor total, caso o pedido concluido ele tambem dara um ticket
# para o usuario com informacoes para entregar e de compra
def comprar_lanches(lanches,comprovante,pedido, nome, endereco):
    while True:
        try:
            lanche_comprar = int(input("Qual lanche o senhor gostaria de comer?\n"))
            break

        except ValueError:
            print("Choose a number")
        
    while True:
        try:
            quantidade = int(input('Digite a quantidade de lancher que o senhor gostaria.\n'))
            break

        except ValueError:
            print('Digite um número')

    print(f'Muito bem, o senhor comprou {quantidade} {lanches[lanche_comprar][0]} pelo valor de R$ {quantidade*lanches[lanche_comprar][1]},00 .')
    
    while True:
        try:
            conf = int(input('Podemos confirmar esse lanche no seu pedido? 0 - Sim | 1 - Nao\n'))
            if conf != 0 or conf != 1:
                print('Digite 1 ou 0')

            if conf == 0 or conf == 1:
                break

        except ValueError:
            print('Digite 0 para confirmar ou 1 para não confirmar')

    if conf == 1:
        mostrar_lanches(lanches)
        comprar_lanches(lanches,comprovante,pedido, nome, endereco)
    
    elif conf == 0:
        pedido = (f'{quantidade} {lanches[lanche_comprar][0]}  por R$ {quantidade*lanches[lanche_comprar][1]},00 \n')
        comprovante += pedido
        
        while True:
            try:
                conf_comp = int(input('Muito Bem, podemos concluir seu pedido ou gostaria de pedir algo mais? 0 - Sim,concluir | 1 - Pedir algo mais\n'))
                if conf_comp != 0 or conf_comp != 1:
                    print("Escolha entre 1 ou 0")

                if conf_comp == 0 and conf_comp == 1:
                    break

            except ValueError:
                print('Escolha entre 1 ou 0')
        
        if conf_comp == 0:
            print(f'Muito bem {nome}')
            print('Voce comprou\n', comprovante)
            print(f'Iremos entregar em {endereco}')

        elif conf_comp == 1:
            mostrar_lanches(lanches)
            comprar_lanches(lanches,comprovante,pedido, nome, endereco)
            
main()        