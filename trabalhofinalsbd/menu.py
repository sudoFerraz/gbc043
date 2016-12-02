"""Interacao com usuario."""


class Menu_inicial(object):
    """Menu inicial para calling do db."""

    def __init__(self):
        """Metodo inicial."""
        self.status = 'Nao logado'
        self.validoptions = [1, 2, 3, 4, 5, 0]
        pass

    def menu(self):
        """Definindo menu inicial."""
        print '\nStatus de usuario:' + self.status
        print '\n[+] Escolha uma opcao para utilizar o lameDB [+]'
        print '\nCriar um novo usuario [1]'
        print '\nLogar com sua conta [2]'
        print '\nResponder um questionario [3]'
        print '\nAtualizar usuario [4]'
        print '\nSair do sistema [0]'
        selection = input()
        if selection == 1:
            self.handle_cria_user()
        elif selection == 2:
            self.handle_logon()
        elif selection == 3:
            self.handle_answer()
        elif selection == 4:
            self.handle_update()
        if selection == 0:
            exit()
        if selection not in self.validoptions:
            print '\n[+] Opcao invalida, saindo do sistema [+]'
            exit()

    def handle_cria_user(self):
        """Criando novo usuario no postgre."""


doido = Menu_inicial()
doido.menu()
