from dotenv import dotenv_values
config = dotenv_values(".env")
CONFIG ={
    "FLASK_DEBUG":config["FLASK_DEBUG"],
    "PORT":config["PORT"]
}