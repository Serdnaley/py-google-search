# Search API

A simple AI-written web search API built with Flask.

## Features

- Perform web searches
- Retrieve search results with titles and snippets
- Swagger UI documentation

## Installation

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```
   python server.py
   ```
2. Access the API at `http://localhost:4000`
3. View Swagger documentation at `http://localhost:4000/docs`

## API Endpoints

- GET `/search?q={query}`: Perform a web search

## Docker

To run the application using Docker:

1. Build the image:
   ```
   docker build -t search-api .
   ```
2. Run the container:
   ```
   docker run -p 4000:4000 search-api
   ```

## License

MIT License