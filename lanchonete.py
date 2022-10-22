import time 
lanches = [('Big Burguer',15),('The crazy cheddar',20),('Morto de Fome',25),('Morte Subita',30)]

#Tela inicial para pegar informacoes pessoas e dizer bem vindo
print('==============================')
print('Bem-Vindo ao GoodFood Delivery')
print('==============================')
print('Gostariamos de lhe conhecer melhor, qual seu o nome ?')
nome = input()
print('Muito bem {}, agora poderia nos dizer seu endereco ? '.format(nome))
endereco = input()
print('Agora ja temos seu endereco de entrega {}, vamos ao pedido.'.format(nome))
print('==============================')
print('Carregando menu')
# time.sleep(1)

#A definicao mostrar lanches fara o cardapio, pegando por ordem os valores importados da lista lanches e enumerando de acordo com a posicao
def mostrar_lanches(lanches):
    print('==============================')
    for i,j in enumerate(lanches):
        print('{} {} R$ {},00'.format(i,j[0],j[1]))

#A definicao comprar_lanches definira o lanche escolhido e a quantidade, ele ira calcular tambem o valor total, caso o pedido concluido ele tambem dara um ticket 
# para o usuario com informacoes para entregar e de compra  
def comprar_lanches():
    print('Qual lanche o senhor gostaria de comer? ')
    lanche_comprar = int(input())
    print('Digite a quantidade de lancher que o senhor gostaria.')
    quantidade = int(input())
    print('Muito bem, o senhor comprou {} {} pelo valor de R$ {},00 .'.format(quantidade,lanches[lanche_comprar][0],quantidade*lanches[lanche_comprar][1]))
    print('Podemos confirmar esse lanche no seu pedido? 0 - Sim | 1 - Nao')
    conf = int(input())
    if conf == 1:
        mostrar_lanches(lanches)
        comprar_lanches()
    elif conf == 0:
        comprovante = ('{} {}  por R$ {},00'.format(quantidade,lanches[lanche_comprar][0],quantidade*lanches[lanche_comprar][1]))
        print('Muito Bem, podemos concluir seu pedido ou gostaria de pedir algo mais? 0 - Sim,concluir | 1 - Pedir algo mais')
        conf_comp = int(input())
        if conf_comp == 0:
            print('Muito bem {}'.format(nome))    
            print('Voce comprou',comprovante)
            print('Iremos entregar em {}'.format(endereco))
        elif conf_comp == 1:
            mostrar_lanches(lanches)
            comprar_lanches()


mostrar_lanches(lanches)
comprar_lanches()

#Essa versao esta com apena 1 bug, quando o usuario pede algo mais o programa nao soma com o anterior, tentei de algumas formas mas ainda nao deu.