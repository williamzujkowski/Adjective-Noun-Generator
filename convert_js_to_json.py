import re
import logging
import os
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to count vowels in a word
def count_vowels(word):
    return sum(1 for char in word if char.lower() in 'aeiou')

# Function to count consonants in a word
def count_consonants(word):
    return sum(1 for char in word if char.lower() in 'bcdfghjklmnpqrstvwxyz')

# Function to check if a word is a palindrome
def is_palindrome(word):
    return word == word[::-1]

# Function to parse data
def parse_data(file_content, prefix, word_type):
    try:
        pattern = re.compile(rf'{prefix}\[\d+\]="(.*?)";')
        words = pattern.findall(file_content)
        return [
            {
                "word": word,
                "type": word_type,
                "first_letter": word[0],
                "length": len(word),
                "vowel_count": count_vowels(word),
                "consonant_count": count_consonants(word),
                "is_palindrome": is_palindrome(word)
            } for word in words
        ]
    except Exception as e:
        logging.error(f"Error parsing data with prefix {prefix}: {e}")
        return []

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except IOError as e:
        logging.error(f"IO error occurred while reading the file: {e}")
    return ""

def main():
    file_path = 'nounadj.js'

    # Ensure the file exists
    if not os.path.exists(file_path):
        logging.error(f"The file {file_path} does not exist.")
        return

    logging.info(f"Reading data from {file_path}")
    file_content = read_file(file_path)
    
    if not file_content:
        logging.error("File content is empty or an error occurred while reading the file.")
        return

    logging.info("Parsing adjectives and nouns")
    adjectives = parse_data(file_content, 'adj', 'adjective')
    nouns = parse_data(file_content, 'noun', 'noun')

    if adjectives:
        logging.info(f"Parsed {len(adjectives)} adjectives")
    else:
        logging.warning("No adjectives found or an error occurred during parsing")

    if nouns:
        logging.info(f"Parsed {len(nouns)} nouns")
    else:
        logging.warning("No nouns found or an error occurred during parsing")

    logging.info("Converting adjectives to JSON")
    adjectives_json_data = json.dumps(adjectives, indent=4)

    logging.info("Converting nouns to JSON")
    nouns_json_data = json.dumps(nouns, indent=4)

    adjectives_output_file_path = 'adjectives.json'
    nouns_output_file_path = 'nouns.json'

    try:
        with open(adjectives_output_file_path, 'w') as json_file:
            json_file.write(adjectives_json_data)
        logging.info(f"Adjectives JSON data written to {adjectives_output_file_path}")
    except IOError as e:
        logging.error(f"IO error occurred while writing the adjectives JSON file: {e}")

    try:
        with open(nouns_output_file_path, 'w') as json_file:
            json_file.write(nouns_json_data)
        logging.info(f"Nouns JSON data written to {nouns_output_file_path}")
    except IOError as e:
        logging.error(f"IO error occurred while writing the nouns JSON file: {e}")

if __name__ == "__main__":
    main()
