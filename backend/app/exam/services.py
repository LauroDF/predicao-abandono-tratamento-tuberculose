from typing import Any

from .repositories import ExamRepository
from ..model.services import ModelService
from ..patient.services import PatientService

from .schemas import ExamDataDTO, PatientExamPayload
from ..patient.schemas import PatientDTO
from ..model.schemas import ModelOutput

class ExamService:
    
    def __init__(self, exam_repo: ExamRepository, model_service: ModelService, patient_service: PatientService) -> None:
        self.exam_repo = exam_repo
        self.model_service = model_service
        self.patient_service = patient_service

    def generate_results(self, data: dict) -> dict:
        payload = PatientExamPayload.model_validate(data)
        patient = payload.PACIENTE
        exam_data = payload.DADOS
        model_id = payload.MODELO
        
        self.patient_service.create_patient(patient)
        model_name = self.model_service.get_model_name(model_id)
        exam_results = self.model_service.predict_with_model(model_id, exam_data)
        saved_record = self.exam_repo.save_exam_record(patient, exam_data, exam_results, model_id, model_name)
        
        return saved_record
    
    def get_all_history(self) -> list[dict]:
        return self.exam_repo.get_all_records()

    def get_exam_data(self, data: dict) -> list[dict]:
        patient = PatientDTO.model_validate(data)
        return self.exam_repo.get_exam_data(patient)
    
    def get_results(self, data: dict) -> list[dict]:
        patient = PatientDTO.model_validate(data)
        return self.exam_repo.get_exam_results(patient)

    def delete_history(self, record_ids: list[str]) -> list[dict]:
        return self.exam_repo.delete_records(record_ids)
    