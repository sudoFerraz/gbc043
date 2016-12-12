import auxiliary
#import objetosbd.py
import sqlalchemy


"""Interacao com usuario."""


class Menu_inicial(object):
    """Menu inicial para calling do db."""

    def __init__(self):
        """Metodo inicial."""
        self.status = 'Nao logado'
        self.validoptions = [1, 2, 3, 4, 5, 0]
        self.Session = auxiliary.connect()
        self.logged = None

    def menu(self):
        """Definindo menu inicial."""
        print '\nStatus de usuario:' + self.status
        print '\n[+] Escolha uma opcao para utilizar o lameDB [+]'
        print '\nCriar um novo usuario [1]'
        print '\nLogar com sua conta [2]'
        print '\nResponder um formulario [3]'
        print '\nAtualizar usuario [4]'
        print '\nCriar um formulario [5]'
        print '\nAlterar um formulario [6]'
        print '\nSair do sistema [0]'
        selection = input()
        if selection == 1:
            newuser = auxiliary.handle_cria_user(self.Session)
            auxiliary.handle_signup(self.Session, newuser)
            self.logged = newuser
        elif selection == 2:
            self.logged = auxiliary.handle_logon(self.Session)
        elif selection == 3:
            check = auxiliary.checkdb(self.session, self.logged)
            auxiliary.choose_form(self.session, self.logged)
        elif selection == 4:
            self.logged = self.handle_update(self.session, self.logged)
        if selection == 0:
            exit()
        if selection not in self.validoptions:
            print '\n[+] Opcao invalida, saindo do sistema [+]'
            exit()



doido = Menu_inicial()
doido.menu()
