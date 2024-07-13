# Adjective-Noun Generator

## Introduction
The Adjective-Noun Generator is a Flask-based application designed to generate random adjective-noun combinations. It's ideal for creative naming, brainstorming sessions, or just for fun. The API uses preloaded JSON files to ensure a vast selection of words and provides various filtering options to customize the generated combinations.

## Features
- Generates random adjective-noun combinations.
- Filters words based on starting letter, length, vowel count, consonant count, and palindrome status.
- User-friendly web interface with help documentation.
- Rate-limited to prevent abuse.
- Dockerized for easy setup and deployment.

## Prerequisites
- Docker
- Docker Compose
- Python 3.12.0 or higher (if running locally without Docker)

## Setup Instructions

### Running Locally

1. **Clone the Repository**:
    ```bash
    git clone https://yourrepositoryurl.com/path/to/repo.git
    cd Adjective-Noun-Generator
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    flask run
    ```

5. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:5000`

### Running with Docker

1. **Build and Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```

2. **Access the Application**:
    Open your browser and go to `http://localhost:5000`

### Deploying to Heroku

1. **Ensure the project directory contains the following files**:
    - `random_word_api.py`
    - `wsgi.py`
    - `runtime.txt`
    - `templates/index.html`
    - `templates/help.html`
    - `adjectives.json`
    - `nouns.json`
    - `Procfile`

2. **Log in to Heroku**:
    ```bash
    heroku login
    ```

3. **Create a Heroku App**:
    ```bash
    heroku create your-app-name
    ```

4. **Deploy to Heroku**:
    ```bash
    git add .
    git commit -m "Deploy to Heroku"
    git push heroku main
    ```

5. **Open the Heroku App**:
    ```bash
    heroku open
    ```

## How to Use

### Web Interface
Once the application is running, you can generate random adjective-noun combinations by using the web interface. The form allows you to specify:
- Number of combinations (1-50)
- Starting letter
- Minimum and maximum word length
- Minimum and maximum vowel count
- Minimum and maximum consonant count
- Whether the words should be palindromes

### Example Request
To generate 10 random combinations starting with the letter "a":
```bash
curl -X POST http://localhost:5000/generate -H "Content-Type: application/json" -d '{
  "num_combinations": 10,
  "letter": "a"
}'
```

### Example Response
```json
[
    {"adjective": "adorable", "noun": "apple"},
    {"adjective": "amazing", "noun": "ant"}
]
```

## Help
For detailed information on how to use the application, visit the [Help Page](http://localhost:5000/help).

## Security
- The API uses Flask-Limiter to rate limit requests and prevent abuse.
- Input validation and sanitization are implemented to prevent injection attacks.
- HTTPS is enforced in production environments.

## Improvements and Contributions
Contributions to improve the application are welcome! Here are some areas for potential improvements:
- Asynchronous processing for better performance under high load.
- Further optimization of memory usage and caching mechanisms.
- Enhanced user interface and experience.

To contribute, fork the repository, make your changes, and submit a pull request.

## Contact
For any queries or contributions, please contact [William Zujkowski](mailto:william.zujkowski@gsa.gov).

## Acknowledgments
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bulma](https://bulma.io/) for the CSS framework.
- [Font Awesome](https://fontawesome.com/) for icons.