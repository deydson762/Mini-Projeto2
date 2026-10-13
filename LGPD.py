from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, DateTime, insert, text
from datetime import datetime

import time
from functools import wraps
def medir_tempo(func):
    """Decorator que mede o tempo de execução de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # tempo inicial (mais preciso que time.time)
        resultado = func(*args, **kwargs)
        fim = time.perf_counter()     # tempo final
        duracao = fim - inicio
        print(f"Função '{func.__name__}' executada em {duracao:.6f} segundos.")
        return resultado
    return wrapper

engine = create_engine("postgresql+psycopg2://alunos:AlunoFatec@200.19.224.150:5432/atividade2", echo=False)
metadata = MetaData()

usuarios = Table(
    'usuarios', metadata,
    Column('id', Integer, primary_key=True),
    Column('nome', String(50), nullable=False, index=True),
    Column('cpf', String(14), nullable=False),
    Column('email', String(100), nullable=False, unique=True),
    Column('telefone', String(20), nullable=False),
    Column('data_nascimento', Date, nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)

@medir_tempo
def LGPD(row):
    row_list = list(row)
    
    # Anonimizar nome (primeira letra de cada palavra, resto com *)
    nome = row_list[1]
    if nome:
        partes = nome.split()
        nome_anonimizado = ' '.join(p[0] + '*' * (len(p) - 1) if len(p) > 1 else p for p in partes)
        row_list[1] = nome_anonimizado
    
    # Anonimizar CPF (primeiros 3 caracteres, resto com *)
    cpf = row_list[2]
    if cpf:
        cpf_anonimizado = cpf[:3] + cpf[3:].replace(cpf[3:-2], '*' * (len(cpf) - 5))
        row_list[2] = cpf_anonimizado
    
    # Anonimizar email (primeira letra, resto com * até o @)
    email = row_list[3]
    if email:
        partes_email = email.split('@')
        if len(partes_email) == 2:
            email_anonimizado = partes_email[0][0] + '*' * (len(partes_email[0]) - 1) + '@' + partes_email[1]
            row_list[3] = email_anonimizado
    
    # Anonimizar telefone (apenas os últimos 4 dígitos)
    telefone = row_list[4]
    if telefone:
        telefone_anonimizado = telefone[-4:]
        row_list[4] = telefone_anonimizado
    
    return tuple(row_list)

users = []
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM usuarios LIMIT 5;"))
    for row in result:
        row = LGPD(row)
        users.append(row)

for user in users:
    print(user)
