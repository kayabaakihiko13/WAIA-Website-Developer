from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define configuration dictionary
CONFIG = {
    "FLASK_DEBUG": os.getenv("FLASK_DEBUG"),
    "PORT": os.getenv("PORT")
}
