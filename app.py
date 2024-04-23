from flask import Flask
from flask_cors import CORS
from src.views import bp as index_bp
from config import CONFIG
def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config['DEBUG'] = CONFIG["FLASK_DEBUG"]
    app.config['PORT'] = int(CONFIG["PORT"])

    # load model
    app.register_blueprint(index_bp)
    return app

if __name__=="__main__":
    app = create_app()
    app.run(port=app.config['PORT'])