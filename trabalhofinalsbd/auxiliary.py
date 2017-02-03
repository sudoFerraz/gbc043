
import objetosbd
import hashlib
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from texttable import Texttable
import uuid
from objetosbd import User, Pessoa, Professor, Aluno, Tecnico, Terceirizado, Unidade_academica, Unidade_administrativa, Curso, Questao, Resposta, Respostas_Possiveis, Formulario
from prettytable import PrettyTable

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
    session.flush()
    return newuser.user


def handle_signup(session, userlogado):
    """Cadastra pessoa e commita no usuario certo."""
    userlogado = str(userlogado)
    print "\nDigite seu nome"
    newnome = raw_input()
    print "\nDigite seu cpf"
    newcpf = raw_input()
    print "\nDigite seu email institucional"
    newinst = raw_input()
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
        session.add(newpessoa)
        session.commit()
        session.flush()
        foundcurso = session.query(Curso).filter_by(sigla=newsig).first()
        if not foundcurso:
            print "Digite o nome do curso"
            newcursoname = raw_input()
            print "Digite a sigla da unidade academica atrelada ao curso"
            newunidacad = raw_input()
            foundunidadeacademica = session.query(Unidade_academica).filter_by(sigla=newunidacad).first()
            if not foundunidadeacademica:
                print "Digite o nome da unidade academica"
                newnomeunidacad = raw_input()
                print "Digite a area de conhecimento"
                newareaconhecimento = raw_input()
                newunidadeacademica = objetosbd.Unidade_academica(sigla=newunidacad, nome=newnomeunidacad, area_conhecimento=newareaconhecimento)
                session.add(newunidadeacademica)
                session.commit()
                session.flush()
            newcurso = objetosbd.Curso(sigla=newsig, nome=newcursoname,\
                                       unidade_academica=newunidacad)
            session.add(newcurso)
            session.commit()
            session.flush()

        #newcurso = objetosbd.Curso(sigla=newsig,)
        newaluno = objetosbd.Aluno(cpf=newcpf, nro_matricula=newmat, curso=newsig)
        session.add(newaluno)
        session.commit()
        print "Cadastro com sucesso, agora voce pode responder formularios\n"

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


def checkdb(session, userlogado):
    """Verifica se existe algum usuario logado, retorna bool."""
    if not userlogado:
        return False
    else:
        return True




def handle_logon(session):
    """Retorna o usuario se estiver logado, False se nao."""
    print "Digite seu user"
    usertry = raw_input()
    print "Digite sua senha"
    passwtry = raw_input()
    founduser = session.query(User).filter_by(user=usertry).first()
    if not founduser:
        print "\nUsuario nao localizado, nao foi possivel efetuar o logon"
        return False
    if founduser.user == usertry:
        if founduser.passw == passwtry:
            print "\nLogado como " + founduser.user
            return founduser.user
        else:
            print "\nUsuario nao localizado, nao foi possivel efetuar o logon"
            return False
    else:
        print "\nUsuario nao localizado, nao foi possivel efetuar o logon"
        return False

def choose_form(session, userlogado):
    j = PrettyTable(['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino'])

    #t = Texttable()
    #t.add_rows([['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino']])
    #nforms = session.query(Formulario).count()
    for form in session.query(Formulario).order_by(Formulario.data_criacao):
        j.add_row([form.nome, form.criador, form.identificador, form.restricao, form.data_criacao, form.data_termino])

    print j
    print "\nDigite o identificador do formulario que voce deseja responder"
    answer = raw_input()
    handle_answer(session, answer, userlogado)

def handle_answer(session, form, userlogged):
    print "Aqui"
    control = 0
    for pess in session.query(Pessoa).filter_by(user=userlogged):
        found = pess.cpf
    for question in session.query(Questao).filter_by(id_formulario=form):
        for answerold in session.query(Resposta).filter_by(cpf_respondedor=found):
            answerold2 = answerold.id_questao
            questionidentificador = question.identificador
            if answerold2 == questionidentificador:
                print "\n\n"
                f = PrettyTable(['Voce ja respondeu a esta questao'])
                print f
                return
        print "\n\n"
        j = PrettyTable(['Descricao>'])
        j.add_row([question.descricao])
        print j
        print "\nResponda a seguir:"
        answer = raw_input()
        newanswer = objetosbd.Resposta(cpf_respondedor=found, id_questao=question.identificador, \
                                       texto_resposta=answer)
        session.add(newanswer)
        #session.flush()

    session.commit()
    print "--------------------------------------------------------------------"


def show_answers(session, userlogged):
    j = PrettyTable(['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino'])

    #t = Texttable()
    #t.add_rows([['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino']])
    #nforms = session.query(Formulario).count()
    for form in session.query(Formulario).order_by(Formulario.data_criacao):
        j.add_row([form.nome, form.criador, form.identificador, form.restricao, form.data_criacao, form.data_termino])

    print j
    print "\nDigite o identificador do formulario que voce deseja responder"
    formid = raw_input()
    for question in session.query(Questao).filter_by(id_formulario=formid):
        questionid = question.identificador
        for answer in session.query(Resposta).filter_by(id_questao=questionid):
            g = PrettyTable(['Cpf Respondedor', 'ID Questao', 'Texto resposta'])
            g.add_row([answer.cpf_respondedor, answer.id_questao, answer.texto_resposta])

    print g






def create_form(session, userlogged):
    print "Digite o nome do formulario"
    formname = raw_input()
    formcreator = userlogged
    print "Digite para quem este formulario e destinado"
    print "Use o formato: tecnicos, terceirizados / todos / professores"
    formrestricao = raw_input()
    formdatecriation = 27
    print "Digite a data de termino deste formulario"
    print "Use o formato dd/mm/aaaa"
    formdateend = raw_input()
    formid = uuid.uuid4()
    formid = hash(formid)
    formid = abs(formid)
    formid = str(formid)
    formid = formid[:5]
    formid = int(formid)
    newform = objetosbd.Formulario(identificador=formid, nome=formname, criador=formcreator, \
                                   restricao=formrestricao, data_criacao=formdatecriation, \
                                   data_termino=formdateend)
    session.add(newform)
    print "Quantas questoes voce deseja adicionar?"
    times = input()
    for i in xrange(0, times, 1):
        print "Digite a descricao da pergunta"
        newdesc = raw_input()
        print "Digite a resposta para a pergunta: 1/0-2-5/sim/nao/blablblabla"
        newanswer = raw_input()
        questionid = uuid.uuid4()
        questionid = hash(questionid)
        questionid = abs(questionid)
        questionid = str(questionid)
        questionid = questionid[:5]
        questionid = int(questionid)
        newquestion = objetosbd.Questao(descricao=newdesc, identificador=questionid, \
                                        id_formulario=formid)
        newresposta = objetosbd.Respostas_Possiveis(id_questao=questionid, \
                                                    resposta=newanswer)
        session.add(newquestion)
        session.add(newresposta)
        print "Formulario criado com sucesso"
    session.commit()

def update_form(session, userlogged):
    j = PrettyTable(['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino'])

    #t = Texttable()
    #t.add_rows([['Nome', 'Criador', 'Identificador', 'Restricao', 'Data criacao', 'Data Termino']])
    #nforms = session.query(Formulario).count()
    for form in session.query(Formulario).order_by(Formulario.data_criacao):
        j.add_row([form.nome, form.criador, form.identificador, form.restricao, form.data_criacao, form.data_termino])

    print j
    t = PrettyTable(['Descricao', 'Identificador'])
    print "Digite o id do formulario que voce deseja alterar"
    formid = raw_input()
    for question in session.query(Questao).filter_by(id_formulario=formid):
        t.add_row([question.descricao, question.identificador])
    print t
    print "\nDigite o id da questao que voce deseja alterar, ou (novo) para adicionar uma nova\
    ou (delete) para deletar uma questao existente"
    target = raw_input()
    if target == 'novo':
        print "Digite a descricao da questao nova"
        newdesc = raw_input()
        questionid = uuid.uuid4()
        questionid = hash(questionid)
        questionid = abs(questionid)
        questionid = str(questionid)
        questionid = questionid[:5]
        questionid = int(questionid)

        print "Digite a resposta para a pergunta: 1/0-2-5/sim/nao/blablblabla"
        newanswer = raw_input()
        newquestion = objetosbd.Questao(descricao=newdesc, identificador=questionid, \
                                        id_formulario=formid)
        newresposta = objetosbd.Respostas_Possiveis(id_questao=questionid, \
                                                    resposta=newanswer)
        session.add(newquestion)
        session.add(newresposta)
    elif target == 'delete':
        print "Digite o id da questao que voce deseja deletar"
        targetid = raw_input()
        session.query(Resposta).filter_by(id_questao=targetid).delete()
        session.query(Questao).filter_by(identificador=targetid).delete()
        session.flush()
    else:
        question = session.query(Questao).filter_by(identificador=target).first()
        print "Digite a nova descricao da pergunta"
        newdesc = raw_input()
        print "Digite a nova resposta da pergunta"
        newanswer = raw_input()
        question.descricao = newdesc
        respostaold = session.query(Respostas_Possiveis).filter_by(id_questao=question.identificador).first()
        respostaold.resposta = newanswer
        session.add(respostaold)
        session.add(question)
        session.flush()

    session.commit()


            #nao esquecer o commit final




    pass

def handle_update(session, userlogged):
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
