ThaiProvinceSearch - Ready-to-run (Version: bundled frontend + backend)

Structure:
  backend/
    app.py           - Flask app (serves API and static frontend)
    provinces.json   - sample provinces data (UTF-8)
    requirements.txt - pip requirements

  frontend/ (static files served by Flask)
    index.html       - Single-page UI (Tailwind CDN)

How to run (Windows PowerShell):
  cd backend
  python -m venv venv
  .\venv\Scripts\activate
  pip install -r requirements.txt
  python app.py

Then open in browser: http://127.0.0.1:5000/

Notes:
  - The API endpoint is available at /api/provinces
  - provinces.json includes sample data (you can replace with your full 77-entry JSON)
