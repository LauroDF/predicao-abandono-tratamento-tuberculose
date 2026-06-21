# Projeto Tuberculose

## Backend API

Este repositório contém um backend em Flask para registrar e recuperar dados de exames de pacientes relacionados à tuberculose.

### Rodando com Docker

- **Observação:** Por padrão, o servidor Flask no projeto está configurado para rodar na porta `7000`.

Passos para build e run (na pasta raiz do projeto):

1. Compor a imagem:

```bash
docker compose up -d
```

2. Acessar a API no navegador ou via curl:

```bash
curl http://localhost:7000/api/health-check
```


### Endpoints disponíveis

- **Health Check:** `GET /api/health-check` — verifica se o servidor está vivo
- **Patient Management:**
	- `POST /api/patient/create` — cria um novo paciente
	- `GET /api/patient/all` — lista todos os pacientes
- **Exam Management:**
	- `POST /api/exam/predict` — gera previsão para dados de exame
	- `GET /api/exam/history` — recupera histórico de exames de um paciente
	- `GET /api/exam/results` — recupera resultados de exames de um paciente
- **Model Management:** `GET /api/model/list` — lista modelos de ML disponíveis

### Contrato da API

Veja [`ENDPOINTS.md`](./ENDPOINTS.md) para detalhes completos dos endpoints, exemplos de requisição, estrutura das respostas e comportamento em caso de erro.