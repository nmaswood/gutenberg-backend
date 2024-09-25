from flask import Flask
from flask_cors import CORS
from routes.book_routes import book_routes
from routes.analysis_routes import analysis_routes


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return "Hello, The App is working"

# Register blueprints (routes)
app.register_blueprint(book_routes)
app.register_blueprint(analysis_routes)

if __name__ == '__main__':
    app.run(debug=True, port=5002)