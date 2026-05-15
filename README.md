# Blog API — FastAPI Backend Project

A backend Blog API project built using FastAPI while learning modern backend development concepts such as authentication, routing, JWT tokens, database relationships, and API structuring.

This project helped me understand how production-style backend applications are organized using modular architecture and reusable components.

---

## Features

- User registration & login
- JWT authentication
- Password hashing
- Create, read, update, and delete blogs
- Protected routes using OAuth2
- SQLAlchemy ORM integration
- Modular router structure
- SQLite database integration

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Authentication & Security
- JWT Tokens
- OAuth2 Password Bearer
- Password Hashing

### Tools
- Pydantic
- Uvicorn

---

## Project Structure

```bash
Blog/
│
├── repository/
│   ├── blog.py
│   └── user.py
│
├── routers/
│   ├── __init__.py
│   ├── authentication.py
│   ├── blog.py
│   └── user.py
│
├── __init__.py
├── database.py
├── hashing.py
├── oauth2.py
├── models.py
├── schemas.py
├── jwt_token.py
├── main.py
│
├── blog.db
├── requirements.txt
└── runtime.txt
```

---

## What I Learned

Through this project, I learned:

- REST API development
- CRUD operations
- API routing with FastAPI
- JWT authentication flow
- OAuth2 authentication system
- Password hashing and security basics
- SQLAlchemy ORM relationships
- Pydantic schema validation
- Modular backend architecture
- Dependency injection in FastAPI
- Database session handling

---

## Authentication Flow

1. User registers an account
2. Password gets hashed before storing
3. User logs in using credentials
4. JWT access token is generated
5. Protected routes require valid bearer token
6. Current authenticated user is extracted using OAuth2 dependency

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd Blog
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Server

```bash
uvicorn main:app --reload
```

---

## API Documentation

FastAPI automatically generates interactive API docs.

### Swagger UI
```bash
http://127.0.0.1:8000/docs
```

### ReDoc
```bash
http://127.0.0.1:8000/redoc
```

---

## Core Concepts Used

- FastAPI Routers
- Dependency Injection
- SQLAlchemy ORM
- JWT Authentication
- OAuth2 Password Bearer
- Password Hashing
- Database Relationships
- API Validation
- Response Models

---

## Future Improvements

- Blog likes & comments
- Pagination
- Search functionality
- Role-based authorization
- PostgreSQL integration
- Docker support
- Unit testing
- Deployment on cloud platforms
- Refresh token system

---

## Purpose of This Project

This project was built as a learning project while exploring backend development with FastAPI. It focuses on understanding authentication systems, backend architecture, API design, and database integration in real-world style applications.
