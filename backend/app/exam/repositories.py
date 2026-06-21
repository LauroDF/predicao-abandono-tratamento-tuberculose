from __future__ import annotations

import json
from datetime import datetime
from json import JSONDecodeError
from pathlib import Path
from uuid import uuid4

from .schemas import ExamDataDTO
from ..patient.schemas import PatientDTO
from ..model.schemas import ModelOutput

class ExamRepository:
    def __init__(self, storage_path: Path | str | None = None) -> None:
        self.storage_path = Path(storage_path) if storage_path else Path(__file__).resolve().parents[2] / "data" / "exam_history.json"
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.storage_path.exists():
            self._write_records([])

    def _read_records(self) -> list[dict]:
        try:
            return json.loads(self.storage_path.read_text(encoding="utf-8"))
        except (JSONDecodeError, FileNotFoundError):
            return []

    def _write_records(self, records: list[dict]) -> None:
        self.storage_path.write_text(
            json.dumps(records, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def save_exam_record(self, user: PatientDTO, exam_data: ExamDataDTO, results: ModelOutput, model_id: str, model_name: str) -> dict:
        records = self._read_records()

        dt_now = datetime.now().isoformat(sep=" ")
        record = {
            "id": str(uuid4()),
            "patient": dict(user),
            "exam_data": dict(exam_data),
            "result": {
                "PROBABILIDADE": results.get("PROBABILIDADE"),
                "CLASSIFICACAO": results.get("CLASSIFICACAO"),
            },
            "model": {
                "id": model_id,
                "name": model_name,
            },
            "timestamp": dt_now,
        }

        records.append(record)
        self._write_records(records)

        return record

    def get_all_records(self) -> list[dict]:
        return self._read_records()

    def get_exam_data(self, user: PatientDTO) -> list[dict]:
        return [
            record["exam_data"]
            for record in self._read_records()
            if record["patient"]["CPF"] == user.CPF
        ]

    def get_exam_results(self, user: PatientDTO) -> list[dict]:
        return [
            record["result"]
            for record in self._read_records()
            if record["patient"]["CPF"] == user.CPF
        ]

    def delete_records(self, record_ids: list[str]) -> list[dict]:
        records = self._read_records()
        filtered = [
            record for record in records
            if record.get("id") not in record_ids
        ]
        self._write_records(filtered)
        return filtered
