# Spoonacular API Flask Application

Esta aplicação é uma API Flask que interage com a API Spoonacular para buscar receitas. A API permite pesquisar receitas por nome e obter detalhes de uma receita específica.

## Estrutura do Projeto

- `app.py`: Contém as rotas e lógica principal da API.
- `README.md`: Documentação do projeto.

## Requisitos

- Python 3.x
- Flask
- requests
- flask_cors

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/eunandocosta/spoonacularapi.git
cd spoonacularapi
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Defina a chave da API Spoonacular no arquivo `app.py`:

```python
SPOONACULAR_API_KEY = 'eaec72804b5c4f34939d2a762312a1a2'
```

Se necessário, você pode obter a chave de API se registrando no [Spoonacular](https://spoonacular.com/food-api).

## Uso

### Iniciar o Servidor

Inicie o servidor Flask:

```bash
flask run
```

A API estará disponível em `http://127.0.0.1:5002`.

### Endpoints

#### Buscar Receitas

Busca receitas pelo nome.

- **URL**: `/recipes`
- **Método**: `GET`
- **Parâmetro de Consulta**: `query` (string)

- **Exemplo**:

  `GET /recipes?query=pasta`

- **Resposta de Sucesso**: `200 OK`

```json
{
    "results": [
        {
            "id": 654959,
            "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
            "image": "https://spoonacular.com/recipeImages/654959-312x231.jpg",
            "imageType": "jpg"
        },
        ...
    ],
    ...
}
```

- **Resposta de Erro**: `400 Bad Request` se o parâmetro `query` não for fornecido.

#### Detalhes da Receita

Busca detalhes de uma receita pelo ID.

- **URL**: `/recipes/<int:recipe_id>`
- **Método**: `GET`

- **Exemplo**:

  `GET /recipes/654959`

- **Resposta de Sucesso**: `200 OK`

```json
{
    "id": 654959,
    "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
    "image": "https://spoonacular.com/recipeImages/654959-556x370.jpg",
    "servings": 2,
    "readyInMinutes": 45,
    "instructions": "...",
    ...
}
```

- **Resposta de Erro**: `Erro ao buscar receitas` se a busca na API Spoonacular falhar.

## Docker

A aplicação pode ser executada usando Docker.

### Dockerfile

O `Dockerfile` define a imagem Docker para a aplicação:

```dockerfile
# Use uma imagem base oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o requirements.txt e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Exponha a porta que o Flask está rodando
EXPOSE 5002

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
```

### docker-compose.yml

O `docker-compose.yml` define os serviços Docker para a aplicação:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5002:5002"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
```

### Usando Docker

1. Construa e inicie os containers Docker:

```bash
docker-compose up --build
```

A API estará disponível em `http://127.0.0.1:5002`.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo `LICENSE` para mais detalhes.
