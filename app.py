# intro
# RESTFull - functions
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Book, Customer, Author
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite'
db.init_app(app)

migrate =Migrate(app, db)


@app.route("/")
def home():
   return jsonify({"message": "Hello world"}), 200

# Authors

# Add Author

@app.route("/authors",  methods=["POST"])
def add_authors():
    # print("Name ", request.json.name)

    data = request.get_json()
    new_author = Author(**data)
    db.session.add(new_author)
    db.session.commit()
    return jsonify({"success": "Author added successfully!"}), 201


# Fetch all authors
@app.route("/authors")
def get_authors():
   authors = Author.query.all()
   authors_list = []

   for author in authors:
      authors_list.append({
         'id':author.id,
         "name": author.name, 
         "yob": author.yob, 
         "nationality": author.nationality, 
      })

   return jsonify({"authors": authors_list}), 200

# Fetch single AUTHOR
@app.route("/authors/<int:author_id>", methods=["GET"])
def get_author(author_id):
   author = Author.query.get(author_id)
   author_list = []

   if author:
        author_list.append({
                'id':author.id,
                "name": author.name, 
                "yob": author.yob, 
                "nationality": author.nationality, 
            })

        return jsonify({"authors": author_list}), 200
   else:
        return jsonify({"error": "Author not found!"}), 404

       


if __name__ =='__main__':
    app.run(port=4000, debug=True)