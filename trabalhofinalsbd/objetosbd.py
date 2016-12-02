"""Definindo as estruturas presentes no bd."""

import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import sqlalchemy
import sys

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    cpf = Column(Integer, primary_key=True)
    nome = Column(String)
    emailinst = Column(String)
    emailsec = Column(String)
    datanasc = Column(String)
    tipo = Column(String)

    def __repr__(self):
        return "<Pessoa(nome='%s', cpf='%s', email institucional='%s',\
        data de nascimento='%s', tipo='%s')>" % (self.nome, self.cpf, \
                                                 self.emailinst, self.datanasc,\
                                                 self.tipo)
#"""
class Professor(Base):
    __tablename__ = 'Professor'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), unique=True, nullable=False)
    siape = Column(Integer, primary_key=True)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'))
    regime_trabalho = Column(Integer)
# Fazer representacao bonita

class Aluno(Base):
    __tablename__ = 'Aluno'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), unique=True, nullable=False)
    nro_matricula = Column(Integer, primary_key=True)
    curso = Column(String)

class Tecnico(Base):
    __tablename__ = 'Tecnico'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), unique=True, nullable=False)
    unidade_administrativa = Column(String, ForeignKey('Unidade_administrativa.sigla'),\
                                    nullable=True)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'),\
                               nullable=True)
    siape = Column(Integer, primary_key=True)

class Terceirizado(Base):
    __tablename__ = 'Terceirizado'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), unique=True,\
                 nullable=False, primary_key=True)
    empresa = Column(String)
    setor_atuacao = Column(String)

class Unicade_academica(Base):
    __tablename__ = 'Unidade Academica'
    sigla = Column(String, primary_key=True)
    nome = Column(String)
    area_conhecimento = Column(String)

class Curso(Base):
    __tablename__ = 'Curso'
    sigla = Column(String, primary_key=True)
    nome = Column(String)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'))

class Unidade_administrativa(Base):
    __tablename__ = 'Unidade Administrativa'
    sigla = Column(String, primary_key=True)
    nome = Column(String)

class Questao(Base):
    __tablename__ = 'Questao'
    descricao_pergunta = Column(String)
    identificador = Column(Integer, primary_key=True)
    resposta = Column(Integer, ForeignKey('Resposta.id'))

class Resposta(Base):
    #0-1, sendo 1 como presente
    __tablename__ = 'Resposta'
    identificador = Column(Integer, primary_key=True)
    texto = Column(String)
    falso = Column(Integer)
    verdadeiro = Column(Integer)
    sim = Column(Integer)
    nao = Column(Integer)
    abstencao = Column(Integer)
    multipla_escolha = Column(Integer) # tratar como uma lista

class Formulario(Base):
    __tablename__ = 'Formulario'
    questoes = Column(Integer, ForeignKey('Questao.identificador'))
    identificador = Column(Integer, primary_key=True)
    nome = Column(String)
    preenchedor = Column(Integer, ForeignKey('Pessoa.cpf'))
    restrito = Column(Integer) #1 prof, 2 aluno, 3 tec, 4 terceirizado
    data_inicio = Column(String)
    data_final = Column(String)

con = None

try:
    con = psycopg2.connect(database='trabalhosbd', user='trabalhosbd', \
                           password='trabalhosbd', host='localhost')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver

except psycopg2.DatabaseError, e:
    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()
#"""
