# Adjective-Noun Generator

## Introduction
The Adjective-Noun Generator is a Flask-based API designed to generate adjective-noun combinations. It's ideal for creative naming, brainstorming sessions, or just for fun. The API uses the NLTK (Natural Language Toolkit) library to ensure that the generated words are valid English words, and Flask-Limiter to manage request rates.

## Features
- Generates random adjective-noun combinations.
- Uses NLTK library for a vast selection of English words.
- Rate-limited to prevent abuse.
- Dockerized for easy setup and deployment.

## Prerequisites
- Docker (optional)
- Python 3.12.2 or higher (if running locally without Docker)
- Heroku CLI (for deployment)

## Setup Instructions
1. Clone the Repository:
   ```sh
   git clone https://yourrepositoryurl.com/path/to/repo.git
   cd adjective_noun_generator
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   flask run
   ```

## Deployment to Heroku
1. Install the Heroku CLI:
   ```sh
   curl https://cli-assets.heroku.com/install.sh | sh
   ```

2. Login to Heroku:
   ```sh
   heroku login
   ```

3. Create a Heroku app:
   ```sh
   heroku create
   ```

4. Deploy the app:
   ```sh
   git push heroku master
   ```

5. Open your app in the browser:
   ```sh
   heroku open
   ```

## How to Use
Once the API is running, you can generate random adjective-noun combinations by accessing the `/generate/<number>` endpoint, where `<number>` is the number of combinations you wish to generate.

**Example Request:**
```sh
curl http://localhost:5000/generate/10
```

**Response:**
```json
{
  "selected_letter": "W",
  "combinations": [
    "wise apple",
    "witty orange",
    ...
  ]
}
```

## Configuration
- The rate limit and other configurations can be adjusted in `random_word_api.py`.
- NLTK data is preloaded in the Docker setup to avoid runtime downloads.

## Development
To contribute or modify the API, set up a development environment by installing the dependencies:
```sh
pip install -r requirements.txt
```
Note: Ensure NLTK datasets (`wordnet` and `averaged_perceptron_tagger`) are downloaded if running outside Docker.

## Security
The API uses Flask-Talisman for HTTPS and security headers. For local testing, HTTPS can be disabled by setting `force_https=False` in `random_word_api.py`.

## Acknowledgments
- [NLTK Project](https://www.nltk.org/) for the datasets.
- [Flask](https://flask.palletsprojects.com/) for the web framework.

## Contact
For any queries or contributions, please contact [William Zujkowski](mailto:william.zujkowski@gmail.com).