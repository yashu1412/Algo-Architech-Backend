# 🚀 Commodity Price API — FastAPI Backend

> **Algo Architech Internship Task | Backend Repository**

A high-performance REST API built with **FastAPI** that acts as a proxy for the [Alpha Vantage](https://www.alphavantage.co/) commodity data API. Provides real-time global commodity price indices with CORS support for the Next.js frontend dashboard.

---

## 📋 Table of Contents

- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [API Reference](#-api-reference)
- [Environment Variables](#-environment-variables)
- [Running the Server](#-running-the-server)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **FastAPI** | REST API framework |
| **Uvicorn** | ASGI server |
| **httpx** | Async HTTP client for Alpha Vantage |
| **python-dotenv** | Manage environment variables |
| **Pydantic** | Request/response data validation |

---

## 📁 Project Structure

```
algo-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # App factory, CORS middleware, router mount
│   ├── routers/
│   │   ├── __init__.py
│   │   └── commodities.py   # GET /api/commodities endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   └── alpha_vantage.py # Async httpx call to Alpha Vantage API
│   └── models/
│       ├── __init__.py
│       └── commodity.py     # Pydantic response schemas
├── .env                     # API key (not committed to git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

| Tool | Minimum Version |
|------|----------------|
| Python | 3.10+ |
| pip | 22.x+ |

### 1. Clone the Repository

```bash
git clone https://github.com/yashu1412/Algo-Architech-Backend.git
cd Algo-Architech-Backend
```

### 2. Create & Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
ALPHA_VANTAGE_API_KEY=demo
```

> 💡 Replace `demo` with a real API key from [alphavantage.co](https://www.alphavantage.co/support/#api-key) for full data access. The free tier provides sufficient data for this dashboard.

---

## 🌐 API Reference

### Base URL
```
http://localhost:8000/api
```

### Endpoints

#### `GET /api/commodities`

Fetches the global commodity price index from Alpha Vantage.

**Query Parameters**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `interval` | string | `monthly` | Data interval: `daily`, `monthly`, or `annual` |

**Example Request**
```bash
curl "http://localhost:8000/api/commodities?interval=monthly"
```

**Example Response**
```json
{
  "name": "Global Price Index of All Commodities",
  "interval": "monthly",
  "unit": "Index 2016=100",
  "data": [
    { "date": "2024-01-01", "value": "140.23" },
    { "date": "2024-02-01", "value": "138.91" }
  ]
}
```

**Error Responses**

| Status | Cause |
|--------|-------|
| `400` | Invalid API key or bad request |
| `429` | Alpha Vantage rate limit reached (free tier: 25 req/day) |
| `500` | Unexpected server error |

### Interactive Docs
Once the server is running, visit:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## ⚙️ Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `ALPHA_VANTAGE_API_KEY` | Yes | `demo` | Alpha Vantage API key |

---

## ▶️ Running the Server

```bash
uvicorn app.main:app --reload --port 8000
```

| Flag | Description |
|------|-------------|
| `--reload` | Auto-restart on code changes (development only) |
| `--port 8000` | Run on port 8000 |

The API will be available at `http://localhost:8000`.

---

## 🔧 CORS Configuration

The API allows cross-origin requests from the frontend development server:

```
http://localhost:3000
http://localhost:3001
```

To add more origins, update `allow_origins` in `app/main.py`.

---

## 🤝 Related Repository

- **Frontend Dashboard:** [Algo-Architech-Frontend](https://github.com/yashu1412/Algo-Architech-Frontend)

---

*Algo Architech | Internship Selection Task 2024*
