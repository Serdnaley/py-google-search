from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from googlesearch import search
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Swagger configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Search API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/search', methods=['GET'])
def perform_search():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    results = [{
        "link": result.url,
        "title": result.title,
        "snippet": result.description,
    } for result in search(query, num_results=20, sleep_interval=3, advanced=True)]

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
