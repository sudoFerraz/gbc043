
import objetosbd.py
import hashlib
import crypto
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

def populate_db():

    pass

def connect():
    """Cria uma conexao e devolve a secao."""
    engine = create_engine('postgresql://scott:tiger@localhost/mydatabase')
    Session = sessionmaker(bind=engine)

    # psycopg2
    #engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
    # pg8000
    #engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
    return Session

def handle_cria_user():
    print "Digite seu nome de usuário"
    user = raw_input()
    print "Digite sua senha"
    passw = raw_input()
    pass

def handle_logon():
    print "\nDigite seu usuário"
    user = raw_input()
    print "\nDigite sua senha:"
    passw = raw_input()

    pass

def handle_answer():
    pass

def handle_update():
    pass


def select_form():
    pass
