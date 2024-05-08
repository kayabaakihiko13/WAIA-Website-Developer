from flask import Blueprint, render_template,request,jsonify
from .models import Note
from . import db
bp = Blueprint("index_views", __name__, template_folder="templates")

@bp.route("/")
def index():
    return render_template("index.html")

# @bp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()  # Parse JSON data from request body

#     # Check if any required fields are missing
#     required_fields = ["firstName", "lastName", "userName", "email", "password_hash"]
#     for field in required_fields:
#         if field not in data:
#             return jsonify({"error": f"Missing required field: {field}"}), 400

#     # Check if username or email already exists
#     existing_user = Users.query.filter_by(userName=data["userName"]).first()
#     if existing_user:
#         return jsonify({"error": "Username already exists"}), 400

#     existing_email = Users.query.filter_by(email=data["email"]).first()
#     if existing_email:
#         return jsonify({"error": "Email already exists"}), 400

#     # Create a new user instance
#     new_user = Users(firstName=data["firstName"], lastName=data["lastName"],
#                      userName=data["userName"], email=data["email"],
#                      password=data["password_hash"])
#     new_user.set_password(data["password_hash"])

#     # Add new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({"message": "User registered successfully"}), 201

# @bp.route("/login",methods=["POST","GET"])
# def login():
#     if request.method == "POST":
#         username = request.form["firstName"]
#         password = request.form["password"]
#     else:
#         return render_template("")
    
@bp.route("/tester")
def tester():
    return jsonify({"message":"connected"})
@bp.route("/note",methods=["POST"])
def note():
    data = request.get_json()
    input_text = Note(text=data["text"])
    db.session.add(input_text)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201
    