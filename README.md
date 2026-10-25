# 🎓 EduTrack — Students Database CRUD Application (+ AI Extension)

[![Python](https://img.shields.io/badge/Python-3.7%2B%20%7C%203.11%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.2-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)](https://www.sqlite.org/)
[![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An individual Python backend engineering project built for the **EWB Edu Tech Pvt. Ltd. Internship Program**. 

The system provides complete **CRUD (Create, Read, Update, Delete)** record operations for managing student data with persistent **SQLite** storage, strict **Pydantic** schema validation, an interactive modern frontend dashboard, auto-generated **OpenAPI/Swagger** documentation, and an optional **Ollama AI** query assistant.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Student Record Schema](#-student-record-schema)
- [API Endpoints Specification](#-api-endpoints-specification)
- [Local Setup & Installation](#-local-setup--installation)
- [Sample API Requests (cURL)](#-sample-api-requests-curl)
- [Optional AI Extension (Ollama)](#-optional-ai-extension-ollama)
- [Cloud Deployment (Render)](#-cloud-deployment-render)
- [Project Evaluation Checklist](#-project-evaluation-checklist)

---

## 📖 Project Overview

Managing student records reliably requires secure data validation, idempotent operations, and clean architectural separation of concerns. This project implements:
1. A decoupled RESTful API layer using **FastAPI**.
2. Object-Relational Mapping (ORM) and persistent storage using **SQLAlchemy** and **SQLite**.
3. A single-page dashboard with real-time KPI metrics, search filtering, and inline editing.
4. An isolated contextual Question-Answering assistant using local large language models (**Ollama** / `llama3.2:1b`) without exposing raw SQL to prompt injection risks.

---

## ✨ Key Features

- **Create**: Add new student profiles with duplicate-email detection and schema validation.
- **Read**: Fetch individual student details by ID or retrieve paginated lists with optional course filters.
- **Update**: Update existing student records partially or completely using `PUT` / `PATCH`.
- **Delete**: Safely delete student profiles with standard HTTP status responses (`200 OK`, `404 Not Found`).
- **Interactive Web UI**: Modern dashboard (`/`) with live KPI counters, real-time client-side search, edit modal, and toast alerts.
- **OpenAPI / Swagger Docs**: Live interactive endpoint testing interface available out-of-the-box at `/docs`.
- **Data Persistence**: Database records persist locally in a file-backed `students.db`.

---

## 🛠 Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend Framework** | FastAPI | High-performance asynchronous API framework |
| **Server** | Uvicorn | Lightning-fast ASGI web server |
| **Database** | SQLite | File-based persistent relational database |
| **ORM** | SQLAlchemy | Python SQL toolkit and Object-Relational Mapper |
| **Validation** | Pydantic | Strict data modeling and request/response validation |
| **HTTP Client** | HTTPX | Async HTTP client for communicating with the AI service |
| **Frontend** | HTML5 / CSS3 / Vanilla JS | Clean administrative dashboard UI with responsive cards |
| **AI Extension** | Ollama (`llama3.2:1b`) | Optional local natural-language database query assistant |

---
# 🎓 EduTrack — Students Database CRUD Application (+ AI Extension)

[![Live Demo](https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://students-database-crud-application.onrender.com/)
[![API Docs](https://img.shields.io/badge/Swagger-Docs-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://students-database-crud-application.onrender.com/docs)

> **Live Application URL**: [https://students-database-crud-application.onrender.com/](https://students-database-crud-application.onrender.com/)  
> **Interactive Swagger Docs**: [https://students-database-crud-application.onrender.com/docs](https://students-database-crud-application.onrender.com/docs)

## 📂 Project Architecture

```text
Students Database CRUD Application/
│
├── app/
│   ├── __init__.py         # Package identifier
│   ├── database.py         # Engine, SessionLocal, Base, get_db dependency
│   ├── models.py           # SQLAlchemy database model
│   ├── schemas.py          # Pydantic request/response validation schemas
│   ├── crud.py             # Reusable database queries & business logic
│   ├── ai_service.py       # Ollama integration helper
│   ├── index.html          # Modern SaaS dashboard frontend
│   └── main.py             # FastAPI entrypoint, routing, and lifecycle
│
├── requirements.txt        # Pinned Python package dependencies
├── README.md               # Project documentation & instructions
├── .gitignore              # Ignores venv, caches, and *.db files
└── render.yaml             # Render cloud infrastructure blueprintgit
