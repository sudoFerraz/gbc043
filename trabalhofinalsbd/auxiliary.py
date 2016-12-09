
import objetosbd
import hashlib
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def populate_db():
    pass

def connect():
    """Cria uma conexao e devolve a secao."""
    engine = create_engine('postgresql://trabalhosbd:trabalhosbd@localhost/trabalhosbd')
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # psycopg2
    #engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase')
    # pg8000
    #engine = create_engine('postgresql+pg8000://scott:tiger@localhost/mydatabase')
    return session

def handle_cria_user(session):
    """Cria novo usario e commita na sessao."""
    print "Digite seu nome de usua rio"
    usernew = raw_input()
    print "Digite sua senha"
    passwnew = raw_input()
    print "Digite seu cpf"
    cpfnew = input()
    newuser = objetosbd.User(user=usernew, passw=passwnew)
    session.add(newuser)
    session.commit()


def handle_logon(session):
    print "Digite seu user"
    usertry = raw_input()
    print "Digite sua senha"
    passwtry = raw_input()
    founduser = session.query(User).filter_by(user=usertry).first()
    if not founduser:
        return False
    if founduser.user == usertry:
        if founduser.passw == passwtry:
            return founduser.cpf
        else:
            return False
    else:
        return False

def handle_answer(session, pessoa, formulario):
    question = session.query(Questao).filter_by(identificador=formulario.questoes).first()
    print question.descricao_pergunta
    print "Responda a seguir:"
    answer = raw_input()

def handle_update():
    pass


def select_form():
    for form in session.query(Formulario).order_by(Formulario.identificador):
        if form.restrito:
            if form.restrito == pessoa.tipo:
                print form.nome
                print "Deseja responder este formulario? s/n"
                if resp == 's':
                    return form.identificador
                if resp == 'n':
                    return
        else:
            print form.nome
            print "Deseja responder este formulario? s/n"
            if resp == 's':
                return form.identificador
            if resp == 'n':
                return
