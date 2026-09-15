# pycodebr-fastapi-car-api

## Comandos úteis

### 1. Instalar o pipx
- `sudo apt install pipx` — instala o gerenciador de ferramentas Python em sistemas baseados em Debian/Ubuntu.
- `pipx ensurepath` — adiciona o diretório do pipx ao PATH do terminal.

### 2. Instalar o Poetry
- `pipx install poetry` — instala o Poetry via pipx.
- `pipx inject poetry poetry-plugin-shell` — adiciona o plugin de shell ao Poetry para melhorar a experiência no terminal.

### 3. Gerenciar o ambiente e dependências
- `poetry install` — instala as dependências do projeto no ambiente virtual do Poetry.
- `poetry add` — adiciona uma nova dependência ao projeto.
- `poetry env info` — mostra informações sobre o ambiente virtual atual.
- `poetry env use 3.13` — define o Python 3.13 como versão do ambiente.
- `poetry python list` — lista as versões do Python disponíveis para o Poetry.
- `poetry python install 3.13` — instala o Python 3.13 para uso no projeto.

### 4. Rodar a aplicação
- `poetry run fastapi dev car_api/app.py --port 8001` — inicia a aplicação FastAPI na porta 8001.

### 5. Criar um novo projeto
- `poetry new --flat car_api` — cria um novo projeto com estrutura simples em uma pasta chamada car_api.

### 6. Inicializar o Alembic
- `poetry run alembic init migrations` — inicializa a estrutura do Alembic no projeto para gerenciar migrações de banco de dados.