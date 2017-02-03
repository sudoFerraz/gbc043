import auxiliary
#import objetosbd.py
import sqlalchemy
from prettytable import PrettyTable


"""Interacao com usuario."""


class Menu_inicial(object):
    """Menu inicial para calling do db."""

    def __init__(self):
        """Metodo inicial."""
        self.status = ''
        self.validoptions = [1, 2, 3, 4, 5, 6, 7, 0]
        self.Session = auxiliary.connect()
        self.logged = None
        self.quitter = 1

    def menu(self):
        """Definindo menu inicial."""
        #print '\nStatus de usuario:' + self.status
        t = PrettyTable(['[+] Opcao', 'Descricao [+]'])
        t.add_row(['[1]', 'Criar um novo usario'])
        t.add_row(['[2]', 'Logar com sua conta'])
        t.add_row(['[3]', 'Responder um formulario'])
        t.add_row(['[4]', 'Atualizar um usuario'])
        t.add_row(['[5]', 'Criar um formulario'])
        t.add_row(['[6]', 'Alterar um formulario'])
        t.add_row(['[7]', 'Mostrar respostas de um formulario'])
        t.add_row(['[0]', 'Sair do sistema'])
        print t
        selection = input()
        if selection == 1:
            newuser = auxiliary.handle_cria_user(self.Session)
            auxiliary.handle_signup(self.Session, newuser)
            self.logged = newuser
            self.status = '\nLogado como' + self.logged
        elif selection == 2:
            self.logged = auxiliary.handle_logon(self.Session)
        elif selection == 3:
            check = auxiliary.checkdb(self.Session, self.logged)
            if check:
                auxiliary.choose_form(self.Session, self.logged)
            else:
                print "Voce nao esta logado, favor entrar"
        elif selection == 4:
            self.logged = auxiliary.handle_update(self.Session, self.logged)
        elif selection == 5:
            auxiliary.create_form(self.Session, self.logged)
        elif selection == 6:
            check = auxiliary.checkdb(self.Session, self.logged)
            if check:
                auxiliary.update_form(self.Session, self.logged)
        elif selection == 7:
            check = auxiliary.checkdb(self.Session, self.logged)
            if check:
                auxiliary.show_answers(self.Session, self.logged)
        if selection == 0:
            exit()
        if selection not in self.validoptions:
            print '\n[+] Opcao invalida, saindo do sistema [+]'
            self.quitter = 0
            exit()


doido = Menu_inicial()
while doido.quitter == 1:
    doido.menu()
