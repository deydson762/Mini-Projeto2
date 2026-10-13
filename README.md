# Mini Projeto 2 - LGPD

Este projeto implementa anonimização de dados pessoais conforme a Lei Geral de Proteção de Dados (LGPD) do Brasil.

## Sobre o Projeto

A LGPD (Lei nº 13.709/2018) estabelece regras sobre coleta, uso, armazenamento e compartilhamento de dados pessoais. Este projeto demonstra técnicas de anonimização para proteger a privacidade de indivíduos.

## Atividades Implementadas

### Atividade 1: Anonimização de Dados
Implementação da função `LGPD` que anonimiza os seguintes campos:
- **Nome**: Substitui letras por asterisco (*), exceto a primeira letra de cada palavra
  - Exemplo: `Olivia Araújo` → `O***** A****`
- **CPF**: Substitui os últimos caracteres por asterisco
  - Exemplo: `237.615.809-59` → `237.***.***-**`
- **E-mail**: Substitui caracteres por * até o @
  - Exemplo: `nuneserick@example.com` → `n*********@example.com`
- **Telefone**: Apresenta apenas os últimos 4 dígitos
  - Exemplo: `+55 (011) 9483-6810` → `6810`

### Atividade 2: Arquivos Separados por Ano
Cria arquivos CSV separados por ano de nascimento, contendo todos os dados anonimizados:
- Cada arquivo é nomeado como `{ano}.csv` (ex: `1990.csv`, `1991.csv`)
- Arquivos são salvos no diretório `arquivos_por_ano/`
- 66 arquivos criados (anos de 1951 a 2011)

### Atividade 3: Arquivo Único
Cria um único arquivo `todos.csv` contendo:
- Apenas os campos `nome` e `cpf`
- Dados **não anonimizados**
- Todos os registros do banco de dados

### Atividade 4: Medição de Tempo
Implementação do decorador `decorator_tempo.py` que:
- Mensura o tempo de execução das atividades 2 e 3
- Grava os tempos em arquivo de log (`execution.log`)
- Utiliza o módulo `logging` do Python

## Configuração do Banco de Dados

- **HOST**: 200.19.224.150
- **USER**: alunos
- **PASSWORD**: AlunoFatec
- **DATABASE**: atividade2

## Requisitos

```bash
pip install -r requirements.txt
```

Dependências:
- SQLAlchemy
- psycopg2-binary
- Faker

## Como Executar

```bash
python LGPD.py
```

O script irá:
1. Executar a Atividade 2 (criar arquivos por ano)
2. Executar a Atividade 3 (criar arquivo único)
3. Registrar os tempos de execução em `execution.log`

## Estrutura do Projeto

```
Mini-Projeto2/
├── LGPD.py                  # Script principal
├── decorator_tempo.py       # Decorator para medição de tempo
├── requirements.txt         # Dependências do projeto
├── README.md               # Este arquivo
├── execution.log           # Log de execução (gerado automaticamente)
├── todos.csv               # Arquivo único com nome e CPF (gerado automaticamente)
└── arquivos_por_ano/       # Diretório com arquivos por ano (gerado automaticamente)
    ├── 1951.csv
    ├── 1952.csv
    ...
    └── 2011.csv
```

## Tabela de Usuários

A tabela `usuarios` possui a seguinte estrutura:
- `id`: Integer (primary key)
- `nome`: String(50)
- `cpf`: String(14)
- `email`: String(100)
- `telefone`: String(20)
- `data_nascimento`: Date
- `created_on`: DateTime
- `updated_on`: DateTime