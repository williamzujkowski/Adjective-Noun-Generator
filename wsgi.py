import os
from random_word_api import app

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "false").lower() in ["true", "1"])