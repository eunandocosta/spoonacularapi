# SpoonacularAPI - API para Buscar Receitas

## Descrição

SpoonacularAPI é uma API desenvolvida para buscar receitas utilizando a API externa Spoonacular. A API permite buscar receitas e obter detalhes de receitas específicas, facilitando o acesso a uma vasta coleção de receitas diretamente do Spoonacular.

## Tecnologias Utilizadas

- **Flask**: Framework de micro serviços para construção de APIs em Python.
- **Flask-CORS**: Extensão para permitir solicitações de outras origens.
- **Requests**: Biblioteca HTTP para fazer requisições à API externa.
- **Docker**: Para containerização da aplicação.
- **Docker Compose**: Para orquestração dos containers.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `Dockerfile`: Arquivo para construir a imagem Docker da aplicação.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.

## Instalação

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos para Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/eunandocosta/spoonacularapi.git
    cd spoonacularapi
    ```

2. Inicie os containers Docker:

    ```bash
    docker-compose up --build
    ```

3. A aplicação estará disponível em `http://localhost:5002`.

## Endpoints

### Buscar Receitas

- **URL**: `/recipes`
- **Método**: `GET`
- **Descrição**: Busca receitas na API Spoonacular com base em um termo de consulta.
- **Parâmetros**:
    - `query`: Termo de busca para as receitas.
- **Exemplo de Requisição**:
    ```bash
    curl "http://localhost:5002/recipes?query=pasta"
    ```
- **Exemplo de Resposta**:
    ```json
    {
        "results": [
            {
                "id": 715538,
                "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
                "image": "https://spoonacular.com/recipeImages/715538-312x231.jpg",
                "imageType": "jpg"
            }
        ],
        "offset": 0,
        "number": 10,
        "totalResults": 86
    }
    ```

### Buscar Detalhes de uma Receita

- **URL**: `/recipes/<int:recipe_id>`
- **Método**: `GET`
- **Descrição**: Busca detalhes de uma receita específica na API Spoonacular.
- **Parâmetros**:
    - `recipe_id`: ID da receita para buscar os detalhes.
- **Exemplo de Requisição**:
    ```bash
    curl "http://localhost:5002/recipes/715538"
    ```
- **Exemplo de Resposta**:
    ```json
    {
        "id": 715538,
        "title": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs",
        "image": "https://spoonacular.com/recipeImages/715538-556x370.jpg",
        "sourceUrl": "http://www.bonappetit.com/recipe/pasta-with-garlic-scallions-cauliflower-breadcrumbs",
        "summary": "Pasta with Garlic, Scallions, Cauliflower & Breadcrumbs might be just the main course you are searching for.",
        "ingredients": [
            {
                "name": "garlic",
                "amount": 2,
                "unit": "cloves"
            }
        ],
        "instructions": [
            {
                "number": 1,
                "step": "Heat the oven to 425 degrees."
            }
        ]
    }
    ```

## Utilizando a API Externa Spoonacular

A API externa Spoonacular é um serviço que fornece informações sobre receitas, ingredientes, nutrição, e muito mais. Para usar a API, você precisa obter uma chave de API do Spoonacular.

### Passos para obter uma chave de API do Spoonacular:

1. Acesse [Spoonacular](https://spoonacular.com/food-api).
2. Crie uma conta ou faça login.
3. Navegue até a seção de API e obtenha a sua chave de API.

### Integração com a API Spoonacular

No código da aplicação, a chave de API é utilizada para autenticar as requisições feitas ao Spoonacular:

```python
SPOONACULAR_API_KEY = 'sua_chave_api_aqui'

@app.route('/recipes', methods=['GET'])
def get_recipes():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Parâmetro 'query' é necessário"}), 400
    
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={SPOONACULAR_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"error": "Erro ao buscar receitas"}), response.status_code

    data = response.json()
    return jsonify(data)
```

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.
