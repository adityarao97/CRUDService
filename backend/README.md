# CRUD Service Backend

A modern Flask-based REST API for managing text entries with SQLite persistence.

## 🚀 Features

- **RESTful API** - Clean and intuitive endpoints
- **SQLite Database** - Lightweight, file-based persistence
- **CORS Support** - Easy cross-origin requests
- **PonyORM** - Elegant database mapping
- **Organized Architecture** - Controllers, Services, Repositories pattern

## 📁 Project Structure

```
backend/
├── app.py                      # Flask application entry point
├── database.py                 # Database configuration
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
├── controllers/               # API route handlers
│   └── text_controller.py
├── services/                  # Business logic
│   └── text_service.py
├── repositories/              # Data access layer
│   └── text_repository.py
├── entities/                  # Database models
│   └── text_entry.py
├── integrations/              # Third-party integrations
│   └── http_client.py
└── data/                      # Database storage
    └── app.db
```

## 🔧 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/adityarao97/CRUDService.git
cd CRUDService/backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Getting Started

Run the development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📡 API Endpoints

### Health Check
- **GET** `/health` - Check if backend is running
  ```bash
  curl http://localhost:5000/health
  ```

### Text Operations
- **POST** `/texts` - Create a new text entry
  ```bash
  curl -X POST http://localhost:5000/texts \
    -H "Content-Type: application/json" \
    -d '{"content": "Your text here"}'
  ```

- **GET** `/texts` - Retrieve all text entries
  ```bash
  curl http://localhost:5000/texts
  ```

## 🛠️ Tech Stack

- **Framework**: Flask
- **ORM**: PonyORM
- **Database**: SQLite
- **CORS**: Flask-CORS
- **HTTP Client**: Requests

## 📋 Requirements

See `requirements.txt` for all dependencies and versions.

## 🔐 Environment Variables

Create a `.env` file in the root directory:
```
FLASK_ENV=development
FLASK_DEBUG=True
```

## 📝 License

MIT License - see LICENSE file for details

## 👤 Author

Aditya Rao

---

**Happy Coding!** 🎉
