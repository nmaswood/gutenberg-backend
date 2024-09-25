from flask import Blueprint, jsonify
from services.gutenberg_service import fetch_book_content, fetch_book_metadata

book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/api/book/<int:book_id>/content', methods=['GET'])
def get_book_content(book_id):
    try:
        content = fetch_book_content(book_id)
        return jsonify({'content': content}), 200  # Format the response here
    except Exception as e:
        return jsonify({'error': str(e)}), 404  # Handle the error and return 404

@book_routes.route('/api/book/<int:book_id>/metadata', methods=['GET'])
def get_book_metadata(book_id):
    try:
        metadata = fetch_book_metadata(book_id)
        return jsonify({'metadata': metadata}), 200  # Format the response here
    except Exception as e:
        return jsonify({'error': str(e)}), 404 