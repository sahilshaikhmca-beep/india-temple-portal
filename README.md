# India Temple Heritage & Pilgrimage Information Portal

A Flask web app that presents structured information about Indian temples and
pilgrimage destinations through a simple, user-friendly interface.

## Features
- Searchable and filterable temple list (name, city, deity, state)
- Detailed temple pages (history, deity, best time to visit, highlights)
- Pilgrimage circuits (Char Dham, Chota Char Dham, Jyotirlingas)
- JSON API at `/api/temples`

## Run locally
    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

Open http://127.0.0.1:5000

## Project structure
- `app.py` – Flask routes
- `data.py` – temple and pilgrimage data
- `templates/` – HTML pages
- `static/css/` – styling

## Add a new temple
Add a dictionary to the `TEMPLES` list in `data.py`.