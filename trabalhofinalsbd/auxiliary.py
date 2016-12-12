
import objetosbd
import hashlib
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from texttable import Texttable


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

def checkdb(session, userlogado):
    pass

def handle_signup(session, userlogado):
    """Cadastra pessoa e commita no usuario certo."""
    print "\nDigite seu nome"
    newnome = raw_input()
    print "\nDigite seu cpf"
    newcpf = raw_input()
    print "\nDigite seu email institucional"
    newint = raw_input()
    print "\nDigite seu email secundario"
    newsec = raw_input()
    print "\nDigite sua data de nascimento"
    newdate = raw_input()
    print "\nVoce e um:"
    print "\n[1] Professor"
    print "\n[2] Aluno"
    print "\n[3] Tecnico"
    print "\n[4] Terceirizado"
    tipo = input()
    if tipo == 1:
        tipo = "Professor"
        print "\nDigite seu numero de SIAPE"
        newsiape = raw_input()
        print "\nDigite seu regime de trabalho"
        newreg = input()
        print "\nDigite a sigla de sua unidade academica"
        newsig = raw_input()
        newpessoa = objetosbd.Pessoa(cpf=newcpf, nome=newnome, emailinst=newinst\
                                     , emailsec=newsec, datanasc=newdate, user=userlogado)
        newprof = objetosbd.Professor(cpf=newcpf, siape=newsiape, unidade_academica=newsig,\
                                       regime_trabalho=newreg)
        session.add(newpessoa)
        session.add(newprof)
        session.commit()
        print "Cadastro com sucesso, agora voce pode responder formularios"
        #Fazer bitmask para permitir a resposta de usuarios novos
    if tipo == 2:
        tipo = "Aluno"
        print "\nDigite seu numero de matricula"
        newmat = raw_input()
        print "\nDigite a sigla de seu curso"
        newsig = raw_input()
        newpessoa = objetosbd.Pessoa(cpf=newcpf, nome=newnome, emailinst=newinst\
                                     , emailsec=newsec, datanasc=newdate, user=userlogado)
        newaluno = objetosbd.Aluno(cpf=newcpf, nro_matricula=newmat, curso=newsig)
        session.add(newpessoa)
        session.add(newaluno)
        session.commit()
        print "Cadastro com sucesso, agora voce pode responder formularios"

    if tipo == 3:
        tipo = "Tecnico"
        print "\nDigite seu numero de SIAPE"
        newsiape = raw_input()
        print "\nDigite o seu setor"
        newsetor = raw_input()
        print "\nDigite a sigla de sua unidade administrativa"
        newadm = raw_input()
        print "\nDigite a sigla de sua unidade academica"
        newacad = raw_input()
        newpessoa = objetosbd.Pessoa(cpf=newcpf, nome=newnome, emailinst=newinst\
                                     , emailsec=newsec, datanasc=newdate, user=userlogado)
        newtecnico = objetosbd.Tecnico(cpf=newcpf, unidade_administrativa=newadm, unidade_academica=newacad,\
                                        siape=newsiape)
        session.add(newpessoa)
        session.add(newtecnico)
        session.commit()
    if tipo == 4:
        tipo = "Terceirizado"
        print "\nDigite o nome de sua empresa"
        newemp = raw_input()
        print "\nDigite o nome do seu setor"
        newsetor = raw_input()
        newpessoa = objetosbd.Pessoa(cpf=newcpf, nome=newnome, emailinst=newinst\
                                     , emailsec=newsec, datanasc=newdate, user=userlogado)
        newterceirizado = objetosbd.Terceirizado(cpf=newcpf, empresa=newemp, setor_atuacao=newsetor)
        session.add(newpessoa)
        session.add(newterceirizado)
        print "Cadastro com sucesso, agora voce pode responder formularios"



def handle_logon(session):
    print "Digite seu user"
    usertry = raw_input()
    print "Digite sua senha"
    passwtry = raw_input()
    founduser = session.query(User).filter_by(user=usertry).first()
    if not founduser:
        print "Usuario nao localizado, nao foi possivel efetuar o logon"
        return False
    if founduser.user == usertry:
        if founduser.passw == passwtry:
            print "Logado como " + founduser.user
            return founduser.user
        else:
            print "Usuario nao localizado, nao foi possivel efetuar o logon"
            return False
    else:
        print "Usuario nao localizado, nao foi possivel efetuar o logon"
        return False

def choose_form(session, userlogado):
    t = Texttable()
    t.add_rows([['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino']])
    #nforms = session.query(Formulario).count()
    for form in session.query(Formulario).order_by(Formulario.data_criacao):
        t.add_rows([[form.nome, form.criador, form.restricao, form.data_criacao, form.data_termino]])

    print t.draw()
    print "\nDigite o identificador do formulario que voce deseja responder"
    answer = raw_input()
    auxiliary.handle_answer(session, answer, userlogado)

def handle_answer(session, form, userlogged):
    for pess in session.query(Pessoa).filter_by(user=userlogged):
        found = pess
    for question in session.query(Questao).filter_by(id_formulario=form):
        print question.descricao
        print "\nResponda a seguir:"
        answer = raw_input()
        newanswer = objetosbd.Resposta(cpf_respondedor=found.cpf, id_questao=question.identificador, \
                                       texto_resposta=answer)
        session.add(newanswer)
    session.commit()


def create_form(session, userlogged):
    pass

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
