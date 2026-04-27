from flask import Flask
from flask_cors import CORS
from database import db
from controllers.text_controller import register_text_route
from entities.text_entry import TextEntry

app = Flask(__name__)
CORS(app)

db.bind(provider="sqlite", filename="data/app.db", create_db=True)
db.generate_mapping(create_tables=True)

register_text_route(app)

if __name__ == "__main__":
    app.run(debug=True)
