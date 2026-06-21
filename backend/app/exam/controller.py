from flask import Blueprint, request, jsonify

from .services import ExamService

def create_exam_blueprint(exam_service: ExamService) -> Blueprint:

    exam_bp = Blueprint('exam_blueprint', __name__)

    @exam_bp.route('/predict', methods=['POST'])
    def create_exam():
        data = request.json or {}
        if not data:
            return jsonify({"error": "Request body vazio"}), 400
        created_exam = exam_service.generate_results(data)
        return jsonify(created_exam), 201
        
    @exam_bp.route('/history', methods=['GET'])
    def get_exam_history():
        history = exam_service.get_all_history()
        return jsonify(history), 200

    @exam_bp.route('/history/delete', methods=['POST'])
    def delete_exam_history():
        data = request.json or {}
        record_ids = data.get('ids', [])
        if not isinstance(record_ids, list):
            record_ids = [record_ids]

        updated_history = exam_service.delete_history(record_ids)
        return jsonify(updated_history), 200
    
    @exam_bp.route('/results', methods=['GET'])
    def get_exam_results():
        data = request.json or {}
        exam_results = exam_service.get_results(data)
        return jsonify(exam_results), 200
        
    return exam_bp