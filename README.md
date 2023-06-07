# Sistema de Gerenciamento de Eventos

### Objetivo: desenvolver um sistema de divulgação, incrição e gerenciamento de eventos

## Tecnologias Utilizadas

* ### Python
* ### Django
* ### Git
* ### PostgreSQL

## Funcionalidades do Projeto
### 1. Página de cadastro de usuário (http://127.0.0.1:8000/cadastro/)
### 2. Página de login de usuário (http://127.0.0.1:8000/login/)
### 3. Página com formulário para cadastro de eventos (http://127.0.0.1:8000/novo_evento/)
### 4. listagem dos eventos cadastrados, filtragem por título e link para inscrição no evento (http://127.0.0.1:8000/gerenciar_evento/)
### 5. página de acesso a um evento específico contendo detalhes como a listagem dos participantes inscritos no evento e botão para fazer a exportação da lista em formato CSV
### 6. Página que lista os eventos nos quais o usuário se inscreveu (http://127.0.0.1:8000/meus_eventos/)
### 7. Geração de certificados para cada evento
### 8. Pesquisa por certificados através do e-mail dos participantes
### 9. Página com a exibição dos certificados gerados para cada participante (http://127.0.0.1:8000/meus_certificados/)

## Instruções para instalação

### Faça o clone do projeto:

```commandline
git clone git@github.com:JulianaRaquel/SISTEMA_DE_EVENTOS.git
```

### Crie o ambiente virtual (venv):
```commandline
python3 -m venv venv
```

### Ative o ambiente virtual no linux:
```commandline
source venv/bin/activate
```

### Ative o ambiente virtual no windows:
```commandline
venv\Scripts\Activate
```

### Instale as dependências:
```commandline
pip install -r requirements.txt
```

### Copie as variáveis de ambiente:
```commandline
cp .env.example .env
```

### Aplique as migrações:
```commandline
python3 manage.py migrate
```

### Rode o servidor:
```commandline
python3 manage.py runserver
```