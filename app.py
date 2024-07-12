from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SPOONACULAR_API_KEY = 'eaec72804b5c4f34939d2a762312a1a2'

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

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe_detail(recipe_id):
    response = requests.get(f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={SPOONACULAR_API_KEY}')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
