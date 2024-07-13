from flask import Flask, jsonify, render_template, request
import json
import random
import os
from functools import lru_cache

app = Flask(__name__)

# Load adjectives and nouns from JSON files
with open("adjectives.json", "r") as f:
    adjectives = json.load(f)

with open("nouns.json", "r") as f:
    nouns = json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@lru_cache(maxsize=128)
def filter_words(
    words, letter, min_length, max_length, min_vowels, min_consonants, is_palindrome
):
    filtered = [
        word
        for word in words
        if (letter == "" or word["first_letter"] == letter)
        and (min_length == 0 or word["length"] >= min_length)
        and (max_length == 0 or word["length"] <= max_length)
        and (min_vowels == 0 or word["vowel_count"] >= min_vowels)
        and (min_consonants == 0 or word["consonant_count"] >= min_consonants)
        and (
            is_palindrome == "either"
            or word["is_palindrome"] == (is_palindrome == "true")
        )
    ]
    return filtered


@app.route("/generate", methods=["POST"])
def generate_words():
    data = request.json

    num_combinations = int(data.get("num_combinations", 10))
    letter = data.get("letter", "a").lower()

    if num_combinations < 1 or num_combinations > 50:
        return jsonify(
            {"error": "Number of combinations must be between 1 and 50"}
        ), 400

    if letter and (len(letter) != 1 or not letter.isalpha()):
        return jsonify(
            {"error": "Starting letter must be a single alphabetic character"}
        ), 400

    min_length = int(data.get("min_length", 1))
    max_length = int(data.get("max_length", 250))
    min_vowels = int(data.get("min_vowels", 1))
    min_consonants = int(data.get("min_consonants", 1))
    is_palindrome = data.get("is_palindrome", "either")

    if is_palindrome not in ["either", "true", "false"]:
        return jsonify({"error": "Invalid value for palindrome"}), 400

    filtered_adjectives = filter_words(
        tuple(adjectives),
        letter,
        min_length,
        max_length,
        min_vowels,
        min_consonants,
        is_palindrome,
    )
    filtered_nouns = filter_words(
        tuple(nouns),
        letter,
        min_length,
        max_length,
        min_vowels,
        min_consonants,
        is_palindrome,
    )

    if (
        len(filtered_adjectives) < num_combinations
        or len(filtered_nouns) < num_combinations
    ):
        return jsonify({"error": "Not enough words matching criteria"}), 400

    selected_adjectives = random.sample(filtered_adjectives, num_combinations)
    selected_nouns = random.sample(filtered_nouns, num_combinations)
    word_pairs = [
        {"adjective": adj["word"], "noun": noun["word"]}
        for adj, noun in zip(selected_adjectives, selected_nouns)
    ]

    return jsonify(word_pairs)


@app.route("/help")
def help():
    return render_template("help.html")


if __name__ == "__main__":
    app.run(debug=True)
