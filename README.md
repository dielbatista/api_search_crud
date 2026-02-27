🚀 API-SEARCH

A API-SEARCH é um projeto de estudo focado no desenvolvimento de uma API CRUD (Create, Read, Update, Delete) robusta. O objetivo central é dominar a comunicação entre uma aplicação Python moderna e um banco de dados SQL, utilizando as melhores práticas de isolamento de ambiente e conteinerização.
🎯 Objetivos do Projeto

Este repositório serve como um laboratório prático para:

    Manipulação de Dados: Realizar operações complexas no banco de dados sem tocar no terminal SQL, delegando tudo ao Python.

    Arquitetura de Software: Entender o papel de um ORM (SQLAlchemy) na abstração da camada de dados.

    Tratamento de Erros: Implementar regras de negócio e validações para garantir a integridade dos dados.

    DevOps iniciante: Orquestrar múltiplos serviços (API + Banco) usando Docker Compose.

🛠 Tecnologias de Peso

O projeto utiliza o que há de mais moderno no ecossistema Python:

    FastAPI: Framework de alta performance, fácil de usar e com documentação automática (Swagger).

    Uvicorn: Servidor ASGI para rodar a aplicação com máxima velocidade.

    SQLAlchemy: A ponte entre o Python e o SQL, permitindo tratar tabelas como classes.

    psycopg2-binary: O driver essencial para a comunicação eficiente com bancos de dados PostgreSQL/SQL.

    Docker: Garante que o projeto rode em qualquer máquina sem conflitos de dependências.

⚙️ Configuração do Ambiente
1. Ambiente Virtual (Local)

Para desenvolver localmente e ter o auxílio do IntelliSense na sua IDE, configure o ambiente virtual:
Bash

# Criar o ambiente virtual
python -m venv venv

# Ativar (Linux/macOS)
source venv/bin/activate

# Ativar (Windows)
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

2. Docker & Docker Compose

A API foi desenhada para rodar dentro de containers. Para subir o banco de dados e o servidor da API simultaneamente:
Bash

docker-compose up -d --build

🏗 Estrutura de Operação

A API gerencia o fluxo de informações da seguinte forma:

    Requisição: O usuário envia um JSON via FastAPI.

    Lógica: O Python processa os dados, aplica regras de negócio e validações.

    Persistência: O SQLAlchemy traduz a lógica para SQL e envia ao container do banco de dados.

    Resposta: O banco confirma a alteração e a API retorna o status para o terminal ou tela.

🛣 Endpoints Disponíveis

Após subir o container, acesse http://localhost:8000/docs para visualizar a documentação interativa:
Funcionalidade	Método	Rota
Listar Usuários	GET	/users
Criar Usuário	POST	/users
Atualizar Dados	PUT	/users/{id}
Remover Usuário	DELETE	/users/{id}

    💡 Nota de Estudo: Este projeto prioriza o entendimento do fluxo de dados e a conteinerização em vez de apenas a entrega de funcionalidades.