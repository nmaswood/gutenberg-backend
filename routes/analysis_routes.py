from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from services.text_analysis_service import identify_characters, sentiment_analysis, summarize_text

# Define the Blueprint
analysis_routes = Blueprint('analysis_routes', __name__)

@analysis_routes.route('/api/analyze-characters', methods=['POST', 'OPTIONS'])
@cross_origin()  # Allow CORS for this specific route
def identify_characters_route():
    if request.method == 'OPTIONS':
        # Handle CORS preflight response
        return '', 200
    data = request.json
    text = data.get('text')
    try:
        analysis_result = identify_characters(text)
        return jsonify({"result": analysis_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@analysis_routes.route('/api/analyze-sentiment', methods=['POST', 'OPTIONS'])
@cross_origin()
def sentiment_analysis_route():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    text = data.get('text')
    try:
        sentiment_result = sentiment_analysis(text)
        return jsonify({"result": sentiment_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@analysis_routes.route('/api/summarize-text', methods=['POST', 'OPTIONS'])
@cross_origin()
def summarize_text_route():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    text = data.get('text')
    try:
        summary_result = summarize_text(text)
        return jsonify({"result": summary_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500