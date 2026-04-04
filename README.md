# Projeto Tarefas

Aplicação web simples para gerenciamento de tarefas, feita com Django.

## Sobre

O sistema permite cadastrar usuários, autenticar, criar tarefas e organizar itens com etiquetas.
Cada tarefa pertence a um usuário, com controle de visibilidade por permissao.

## Funcionalidades

- Cadastro e login de usuários
- Criacao, edicao e remocao de tarefas
- Busca por titulo e descricao
- Etiquetas para classificacao
- Permissao especial para visualizar tarefas de todos os usuários

## Stack

- Python 3.13
- Django 5.2
- SQLite

## Estrutura principal

- `core/`: configuração do projeto Django
- `tarefas/`: app principal (models, views, templates, urls)
- `db.sqlite3`: banco de dados local

## Como rodar localmente

### 1. Criar e ativar ambiente virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 3. Aplicar migrações

```powershell
python manage.py migrate
```

### 4. Executar servidor

```powershell
python manage.py runserver
```

Acesse no navegador:

- http://127.0.0.1:8000/tarefas/

## Rotas principais

- `/tarefas/` - pagina inicial
- `/tarefas/login/` - login
- `/tarefas/register/` - cadastro
- `/tarefas/adicionar/` - adicionar tarefa
- `/tarefas/buscar/` - buscar tarefas

## Observacoes

- Em ambiente de desenvolvimento, o banco SQLite é criado localmente no arquivo `db.sqlite3`.
- Caso ocorra erro de tabela ausente, execute novamente `python manage.py migrate`.
