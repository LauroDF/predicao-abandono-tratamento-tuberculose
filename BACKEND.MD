# Projeto Tuberculose

## Backend API

This repository contains a Flask-based backend for recording and retrieving patient exam data related to tuberculosis.


### Available endpoints

**Health Check:**
- `GET /api/health-check` — verify server liveness

**Patient Management:**
- `POST /api/patient/create` — create a new patient
- `GET /api/patient/all` — list all patients

**Exam Management:**
- `POST /api/exam/predict` — generate prediction for exam data
- `GET /api/exam/history` — retrieve exam history for a patient
- `GET /api/exam/results` — retrieve exam results for a patient

**Model Management:**
- `GET /api/model/list` — list available ML models

### API contract

See [`ENDPOINTS.md`](./ENDPOINTS.md) for full endpoint details, example requests, response structure, and error behavior.
