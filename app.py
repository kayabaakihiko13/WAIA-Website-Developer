from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from src.views import bp as index_bp
from src import db
from config import UPLOAD_PATH
def create_app() -> Flask:
    load_dotenv()
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]= os.environ.get("DB_URL")
    app.config["UPLOAD_FOLDER"] =UPLOAD_PATH 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    CORS(app)
    # load model
    app.register_blueprint(index_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    # Run the Flask application
    app.run(debug=True)

