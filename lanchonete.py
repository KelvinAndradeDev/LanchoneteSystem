class Lanchonete:

    def __init__(self):
        self.lanches = [('Big Burguer', 15), ('The crazy cheddar', 20),
                        ('Morto de Fome', 25), ('Morte Subita', 30)]

        self.comprovante = ''
        self.pedido = ''
        self.nome = self.take_name()
        self.endereco = self.take_adress()
        self.mostrar_lanches()
        self.comprar_lanches()

    # Tela inicial para pegar informacoes pessoas e dizer bem vindo
    def take_name(self):
        print('==============================')
        print('Bem-Vindo ao GoodFood Delivery')
        print('==============================')
        print('Gostariamos de lhe conhecer melhor, qual seu o nome ?')
        nome = input()
        return nome
    # time.sleep(1)

    def take_adress(self):
        print(f'Muito bem {self.nome}, agora poderia nos dizer seu endereco ? ')
        adress = input()
        print(f'Agora ja temos seu endereco de entrega {self.nome}, vamos ao pedido.')
        print('==============================')
        print('Carregando menu')
        return adress


    # A definicao mostrar lanches fara o cardapio, pegando por ordem os valores importados da lista lanches e enumerando de acordo com a posicao
    def mostrar_lanches(self):
        print('==============================')
        for i, j in enumerate(self.lanches):
            print(f'{i} {j[0]} R$ {j[1]},00')

    # A definicao comprar_lanches definira o lanche escolhido e a quantidade, ele ira calcular tambem o valor total, caso o pedido concluido ele tambem dara um ticket
    # para o usuario com informacoes para entregar e de compra
    def comprar_lanches(self):
        while True:
            try:
                lanche_comprar = int(input("Qual lanche o senhor gostaria de comer? Escolha entre 0-3\n"))
                break

            except (ValueError, IndexError):
                print("Choose a number between 0-3")

            
        while True:
            try:
                quantidade = int(input('Digite a quantidade de lancher que o senhor gostaria.\n'))
                break

            except ValueError:
                print('Digite um número')

        print(f'Muito bem, o senhor comprou {quantidade} {self.lanches[lanche_comprar][0]} pelo valor de R$ {quantidade * self.lanches[lanche_comprar][1]},00 .')

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
            self.mostrar_lanches()
            self.comprar_lanches()

        elif conf == 0:
            pedido = (f'{quantidade} {self.lanches[lanche_comprar][0]}  por R$ {quantidade * self.lanches[lanche_comprar][1]},00 \n')
            self.comprovante += self.pedido
            
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
                print(f'Muito bem {self.nome}')
                print('Voce comprou\n', self.comprovante)
                print(f'Iremos entregar em {self.endereco}')

            elif conf_comp == 1:
                self.mostrar_lanches()
                self.comprar_lanches()
