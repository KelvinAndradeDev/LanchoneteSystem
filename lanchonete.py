import time
lanches = [('Big Burguer', 15), ('The crazy cheddar', 20),
           ('Morto de Fome', 25), ('Morte Subita', 30)]
comprovante = ''

def main():
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
comprovante = ' '
pedido = ''
def mostrar_lanches(lanches):
    print('==============================')
    for i, j in enumerate(lanches):
        print(f'{i} {j[0]} R$ {j[1]},00')

# A definicao comprar_lanches definira o lanche escolhido e a quantidade, ele ira calcular tambem o valor total, caso o pedido concluido ele tambem dara um ticket
# para o usuario com informacoes para entregar e de compra

def comprar_lanches(lanches,comprovante,pedido, nome, endereco):
    print('Qual lanche o senhor gostaria de comer? ')
    lanche_comprar = int(input())
    print('Digite a quantidade de lancher que o senhor gostaria.')
    quantidade = int(input())
    print(f'Muito bem, o senhor comprou {quantidade} {lanches[lanche_comprar][0]} pelo valor de R$ {quantidade*lanches[lanche_comprar][1]},00 .')
    print('Podemos confirmar esse lanche no seu pedido? 0 - Sim | 1 - Nao')
    conf = int(input())
    if conf == 1:
        mostrar_lanches(lanches)
        comprar_lanches(lanches,comprovante,pedido, nome, endereco)
    elif conf == 0:
        pedido = (f'{quantidade} {lanches[lanche_comprar][0]}  por R$ {quantidade*lanches[lanche_comprar][1]},00 \n')
        comprovante =  comprovante + pedido
        print('Muito Bem, podemos concluir seu pedido ou gostaria de pedir algo mais? 0 - Sim,concluir | 1 - Pedir algo mais')
        conf_comp = int(input())
        if conf_comp == 0:
            print(f'Muito bem {nome}')
            print('Voce comprou\n', comprovante)
            print(f'Iremos entregar em {endereco}')
        elif conf_comp == 1:
            # comprovante = comprovante +  pedido
            mostrar_lanches(lanches)
            comprar_lanches(lanches,comprovante,pedido, nome, endereco)
            

main()
