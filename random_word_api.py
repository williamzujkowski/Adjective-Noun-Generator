"""
random_word_api.py
This module provides a Flask-based API for generating random adjective-noun combinations.
The API is secured with Flask-Talisman for HTTPS and security headers, and Flask-Limiter for rate limiting.
"""

from flask import Flask, jsonify, abort
import nltk
from nltk.corpus import wordnet as wn
import random
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)

# Check if we are in a development environment
is_dev = os.environ.get("FLASK_ENV") == "development"

# Apply HTTP security headers, conditionally enforce HTTPS
Talisman(app, force_https=not is_dev)

# Configure Flask-Limiter to use in-memory storage
limiter = Limiter(
    app=app, key_func=get_remote_address, default_limits=["100 per day", "20 per hour"]
)

# Download necessary NLTK data
nltk.download("wordnet", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)


def is_appropriate(word):
    """Check for appropriateness of the word."""
    for synset in wn.synsets(word):
        if "offensive" in synset.definition().lower():
            return False
    return True


def get_filtered_words(pos, chosen_letter, limit=1000):
    """Retrieve and filter words based on POS and starting letter."""
    words = set()
    for synset in wn.all_synsets(pos=pos):
        for lemma in synset.lemmas():
            word = lemma.name().replace("_", " ").lower()
            if (
                word.startswith(chosen_letter)
                and word not in words
                and is_appropriate(word)
            ):
                words.add(word)
            if len(words) >= limit:
                break
    return list(words)


@app.route("/generate/<int:num_combinations>", methods=["GET"])
@limiter.limit("10 per minute")  # Apply rate limiting to this endpoint
def generate_combinations(num_combinations):
    """Generate adjective-noun combinations based on a random letter."""
    if num_combinations <= 0 or num_combinations > 50:  # Validate input
        abort(400, description="Number of combinations must be between 1 and 50.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chosen_letter = random.choice(alphabet)
    adjectives = get_filtered_words("a", chosen_letter, limit=1000)
    nouns = get_filtered_words("n", chosen_letter, limit=1000)

    combinations = []
    for _ in range(num_combinations):
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        combinations.append(f"{adj} {noun}")

    return jsonify(
        {"selected_letter": chosen_letter.upper(), "combinations": combinations}
    )


@app.errorhandler(400)
def bad_request(error):
    """Handle 400 errors with a JSON response."""
    return jsonify(error=str(error.description)), 400


@app.errorhandler(429)
def rate_limit_exceeded(error):
    """Handle 429 errors with a JSON response."""
    return jsonify(error="Rate limit exceeded. Please try again later."), 429


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() in ["true", "1"])