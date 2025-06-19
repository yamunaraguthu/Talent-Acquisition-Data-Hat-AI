#FASTAPI BACKEND FOR NEWS & WEATHER aGGREGATION

DATA-HAT BACKEND DEVELOPER ASSIGNMENT
SUBMITTED BY NAME:RAGUTHU YAMUNA

TASK:Build a FastAPI Backend for News & Weather Aggregation












🚀Requirements

User authentication (signup, login, logout) using JWT tokens

News aggregation (requires authentication) via NewsAPI

Weather data aggregation (no authentication needed)

Swagger documentation available at /docs

Caching to reduce load on third-party APIs

---

🛠 Tech Stack

Python (3.12.6)

FastAPI

JWT for authentication

NewsAPI / OpenWeatherMap (or similar)

---

⚡ Setup & Installation

1️⃣ Clone the repository

git clone https://github.com/yamunaraguthu/Talent-Acquision-Data-Hat-AI
cd data-hat-backend

2️⃣ Create a virtual environment

python -m venv yamuna
yamuna\Scripts\activate     

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Set up environment variables

Create a .env file based on .env.example:

SECRET_KEY=kw4dJvpSGD_XN-n_zFy_SnAmiM_WL9PV_d1DjolHr3o
NEWS_API_KEY=7b292e04a7ac4bb59f787de6e9fbed04
WEATHER_API_KEY=767c1905e7ab50e9f6751515fd1e7d46
REDIS_URL="redis://localhost:6379/0"

5️⃣ Run the app

uvicorn app.main:app --reload

---

📌 Authentication Endpoints

POST /signup — Register a new user

POST /login — Login and receive JWT token

POST /logout — Invalidate token

---

📌 News Endpoints

Route:GET/news
Description:Fetches top headlines or search-based news using NewsAPI
query Param:Search(Optional)

---

📝 Example Responses

Weather
{
  "count": 1,
  "location": "Srikakulam",
  "unit": "metric",
  "data": [
    {
      "date": "Thu June 19 2025",
      "main": "Clouds",
      "temp": 28.13
    }
  ]

---

Use FastAPI (Python 3.12.6)
• Use JWT or similar for authentication
• Return all API responses in JSON
• Provide Swagger docs at /docs
• Write a README.md for setup and usage
• Use caching to reduce third-party API load





