from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from views import bp as index_bp

def create_app() -> Flask:
    app = Flask(__name__)
    load_dotenv()
    CORS(app)
    # load model
    app.register_blueprint(index_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    # Run the Flask application
    app.run(debug=bool(os.getenv("FLASK_DEBUG")), port=int(os.getenv("PORT")))

