# CRUD Service

A full-stack text management application with a **Python Flask backend** and **React Vite frontend** for achieving basic CRUD functionality.

## 📋 Overview

A simple yet powerful application that allows users to create, read text entries through an intuitive web interface. The project demonstrates a clean separation of concerns with a RESTful API backend and a modern reactive frontend.

## 🏗️ Architecture

```
Root/
├── backend/                    # Python Flask REST API
│   ├── app.py
│   ├── database.py
│   ├── controllers/
│   ├── services/
│   ├── repositories/
│   ├── entities/
│   └── README.md
│
└── frontend/                   # React + Vite Application
    ├── src/
    ├── components/
    ├── App.jsx
    └── README.md
```

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend runs on: `http://localhost:5000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

## ✨ Features

- ✅ **Create** - Add new text entries
- ✅ **Read** - Fetch all stored texts
- ✅ **Database** - SQLite persistence
- ✅ **API** - RESTful endpoints with CORS support
- ✅ **UI** - Modern React interface with Vite
- ✅ **Error Handling** - Robust error management

## 📡 API Endpoints

- `GET /health` - Health check
- `POST /texts` - Create a text entry
- `GET /texts` - Retrieve all text entries

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask
- **ORM**: PonyORM
- **Database**: SQLite
- **CORS**: Flask-CORS

### Frontend
- **Library**: React
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **Runtime**: Node.js

## 📚 Documentation

- [Backend README](./backend/README.md) - Detailed backend documentation
- [Frontend README](./frontend/README.md) - Detailed frontend documentation

## 🔧 Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

## 📝 License

MIT License

## 👤 Author

Aditya Rao

---

**Start building!** 🎉
