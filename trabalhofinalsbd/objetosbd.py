"""Definindo as estruturas presentes no bd."""

import psycopg2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Gerar as classes na tabela:

# gabriel = Pessoa(cpf=123, nome='Gabriel'...)
# session.add(gabriel)
# session.commit()
# print(gabriel.cpf)

class User(Base):
    __tablename__ = 'User'
    user = Column(String, primary_key=True)
    passw = Column(String)

class Pessoa(Base):
    __tablename__ = 'Pessoa'
    cpf = Column(Integer, primary_key=True)
    nome = Column(String)
    emailinst = Column(String)
    emailsec = Column(String)
    datanasc = Column(String)
    user = Column(String, ForeignKey('User.user'))


class Professor(Base):
    __tablename__ = 'Professor'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), nullable=False)
    siape = Column(Integer, primary_key=True)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'))
    regime_trabalho = Column(Integer)
# Fazer representacao bonita

class Aluno(Base):
    __tablename__ = 'Aluno'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), nullable=False)
    nro_matricula = Column(String, primary_key=True)
    curso = Column(String, ForeignKey('Curso.sigla'))

class Tecnico(Base):
    __tablename__ = 'Tecnico'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), nullable=False)
    unidade_administrativa = Column(String, ForeignKey('Unidade_administrativa.sigla'),\
                                    nullable=True)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'),\
                               nullable=True)
    siape = Column(Integer, primary_key=True)

class Terceirizado(Base):
    __tablename__ = 'Terceirizado'
    cpf = Column(Integer, ForeignKey('Pessoa.cpf'), primary_key=True)
    empresa = Column(String)
    setor_atuacao = Column(String)

class Unidade_academica(Base):
    __tablename__ = 'Unidade_academica'
    sigla = Column(String, primary_key=True)
    nome = Column(String)
    area_conhecimento = Column(String)

class Curso(Base):
    __tablename__ = 'Curso'
    sigla = Column(String, primary_key=True)
    nome = Column(String)
    unidade_academica = Column(String, ForeignKey('Unidade_academica.sigla'))

class Unidade_administrativa(Base):
    __tablename__ = 'Unidade_administrativa'
    sigla = Column(String, primary_key=True)
    nome = Column(String)

class Questao(Base):
    __tablename__ = 'Questao'
    descricao = Column(String)
    identificador = Column(Integer, primary_key=True)
    id_formulario = Column(Integer, ForeignKey('Formulario.identificador'), \
                          nullable=True)

class Resposta(Base):
    #0-1, sendo 1 como presente
    __tablename__ = 'Resposta'
    cpf_respondedor = Column(Integer, ForeignKey('Pessoa.cpf'), primary_key=True)
    id_questao = Column(Integer, ForeignKey('Questao.identificador'), primary_key=True)
    texto_resposta = Column(String)

class Respostas_Possiveis(Base):
    __tablename__ = 'Respostas_Possiveis'
    id_questao = Column(Integer, ForeignKey('Questao.identificador'), primary_key=True)
    resposta = Column(String)

class Formulario(Base):
    __tablename__ = 'Formulario'
    identificador = Column(Integer, primary_key=True)
    nome = Column(String)
    criador = Column(String)
    restricao = Column(String)
    data_criacao = Column(String)
    data_termino = Column(String)


engine = create_engine('postgresql://trabalhosbd:trabalhosbd@localhost/trabalhosbd')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
