# Text CRUD App

A React + Vite frontend application for managing text entries with a RESTful API backend.

## Features

- Create new text entries
- View all saved texts in a list
- Error handling for failed API requests
- Real-time state management with React hooks

## Project Structure

```
src/
├── api.js              # API service with axios
├── App.jsx             # Main app component with state management
├── index.jsx           # Entry point
└── components/
    ├── TextForm.jsx    # Form component for creating texts
    └── TextList.jsx    # List component for displaying texts
```

## Setup Instructions

### Prerequisites
- Node.js and npm installed
- Backend API running on `http://localhost:5000`

### Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173`

## Dependencies

- **react**: UI framework
- **vite**: Build tool and dev server
- **axios**: HTTP client for API requests

## API Endpoints

The app communicates with the following backend endpoints:

- `POST /texts` - Create a new text entry
- `GET /texts` - Retrieve all text entries

## Development

This project uses:
- **Vite** for fast development and building
- **ESLint** for code quality
- **React Compiler** for optimized performance

## Browser DevTools

For better debugging experience, install [React DevTools](https://react.dev/link/react-devtools) browser extension.
