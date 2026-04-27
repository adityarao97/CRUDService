from flask import request, jsonify
from services.text_service import TextService

text_service = TextService()


def register_text_route(app):

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"message": "Backend is running"}), 200

    @app.route("/texts", methods=["POST"])
    def create_text():
        data = request.get_json()
        content = data.get("content") if data else None
        result, status_code = text_service.create_text(content)
        return jsonify(result), status_code

    @app.route("/texts", methods=["GET"])
    def get_all_texts():
        result, status_code = text_service.get_all_text()
        return jsonify(result), status_code
