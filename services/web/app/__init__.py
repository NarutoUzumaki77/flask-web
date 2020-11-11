from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from .model import user_table


@app.route("/")
def hello_world():
    return jsonify({"message": "hello world from flask-web"})


@app.route("/config")
def config():
    return jsonify({"database": app.config["SQLALCHEMY_DATABASE_URI"]})


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return f"""
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """


@app.route("/users", methods=["POST"])
def createUser():
    name = request.json.get("name")
    username = request.json.get("username")
    email = request.json.get("email")

    try:
        user = user_table.User(
            name=name,
            username=username,
            email=email
        )
        user.create()

        return jsonify({"message": "user created"}), 201

    except Exception as ex:
        return jsonify({"message": str(ex)}), 400


@app.route("/users")
def getAllUsers():
    users = db.session.query(user_table.User).all()
    formatted_msg = [user.format() for user in users]
    return jsonify(formatted_msg), 200


