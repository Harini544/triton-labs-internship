# Task Management API

A beginner-friendly FastAPI project for managing users and tasks. The project is intentionally modular so each part is easy to explain during an internship review.

## Features

- Health-check endpoint
- User create, list, retrieve, update, and delete endpoints
- Task create, list, retrieve, update, and delete endpoints
- Pydantic request and response validation
- In-memory storage through service classes
- Environment-based configuration
- Pytest test suite

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- python-dotenv
- pytest

## Project Structure

```text
task-management-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── tests/
├── requirements.txt
├── .gitignore
├── README.md
└── .env.example
```

## Setup Instructions

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the API:

```powershell
uvicorn app.main:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

Run tests:

```powershell
pytest
```

## Example API Endpoints

- `GET /health`
- `POST /users/`
- `GET /users/`
- `GET /users/{user_id}`
- `PATCH /users/{user_id}`
- `DELETE /users/{user_id}`
- `POST /tasks/`
- `GET /tasks/`
- `GET /tasks/{task_id}`
- `PATCH /tasks/{task_id}`
- `DELETE /tasks/{task_id}`

Example user request:

```json
{
  "name": "Asha Rao",
  "email": "asha@example.com"
}
```

Example task request:

```json
{
  "title": "Write README",
  "description": "Document setup and API usage.",
  "status": "todo",
  "user_id": 1
}
```

## Git Workflow Notes

Create a feature branch before working:

```powershell
git checkout -b feature/task-management-api
```

Make focused commits with clear messages:

```powershell
git add .
git commit -m "Build modular FastAPI task management API"
git push -u origin feature/task-management-api
```

## Security Note

Never commit `.env` files, API keys, passwords, tokens, or other secrets. Use `.env.example` to document expected environment variables without real secret values.
