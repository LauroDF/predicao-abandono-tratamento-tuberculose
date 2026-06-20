# 🫁 TB Predict

## Sobre o Projeto

O TB Predict é uma aplicação web desenvolvida para auxiliar na predição da probabilidade de abandono do tratamento da tuberculose. O sistema permite o preenchimento de informações clínicas, sociais e demográficas do paciente, gerando uma estimativa de risco baseada em um modelo de Inteligência Artificial.

Atualmente o frontend está totalmente funcional, incluindo validações, histórico de consultas e interface responsiva. A integração com o modelo de Machine Learning será realizada pelo backend.

---

## Funcionalidades

### Predição

* Cadastro de pacientes;
* Preenchimento de fatores clínicos e sociais;
* Validação dos campos obrigatórios;
* Simulação da probabilidade de abandono do tratamento;
* Exibição do resultado em percentual.

### Histórico

* Armazenamento local das predições realizadas;
* Visualização dos pacientes cadastrados;
* Ordenação por nome e probabilidade;
* Exibição detalhada das informações;
* Seleção individual ou múltipla de registros;
* Remoção dos registros selecionados.

### Usabilidade

* Modo claro e escuro (Dark Mode);
* Máscara automática para CPF;
* Validação de idade mínima;
* Restrição de caracteres nos campos de entrada.

---

## Tecnologias Utilizadas

* HTML5
* CSS3
* JavaScript (Vanilla JS)
* LocalStorage
* Python (3.12)
* Flask

---

## Estrutura do Projeto

```text
predicao-abandono-tratamento-tuberculose/
├── BACKEND.MD
├── ENDPOINTS.md
├── README.md
├── backend/        # API Flask e integração com modelos
│   ├── requirements.txt
│   ├── run.py
|   ├── logs/                
│   └── app/
│       ├── __init__.py
│       ├── error_handlers.py
│       ├── exceptions.py
│       ├── logger.py
│       ├── service_registry.py
│       ├── exam/     
│       ├── healthcheck/
│       ├── model/
│       └── patient/
├── frontend/       # Frontend (HTML/CSS/JS)
│   ├── index.html
│   ├── historico.html
│   └── style.css
├── models/         # Notebooks e artefatos dos modelos
│   ├── logistic_regression_model.ipynb
│   ├── neural_network_model.ipynb
│   ├── xgboost_model.ipynb
│   ├── logistic_regression/ 
│   ├── nn_keras/            
│   └── xg_boost/           
└── preprocessing/  # Artefatos de pré-processamento
```

---

## Fluxo de Funcionamento

1. O usuário preenche os dados do paciente.
2. O sistema valida todas as informações inseridas.
3. Os dados são enviados para o modelo de predição.
4. A probabilidade de abandono é exibida na tela.
5. O resultado é armazenado no histórico para futuras consultas.

---

## Melhorias Futuras

* Persistência em banco de dados;
* Sistema de autenticação de usuários;
* Dashboard analítico;
* Exportação de relatórios;
* Cadastro de profissionais de saúde.

---

## Integrantes

* Augusto Rosso
* Felipe Bacchi
* Gabriel Mascarenhas
* Lauro Dariva Ferneda
* Pedro Augusto
* Pedro Leal

---

## Licença

Projeto desenvolvido para fins acadêmicos.