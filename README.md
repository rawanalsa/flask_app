# Flask Task Manager

A simple Flask + SQLAlchemy task manager with create, update, and delete actions. Tasks are stored in a local SQLite database in the `instance/` folder.

## Features
- Add tasks
- Update tasks
- Delete tasks
- SQLite persistence (auto-created)

## Tech Stack
- Flask
- Flask-SQLAlchemy
- Flask-Scss
- SQLite

## Project Structure
```
.
├── app.py
├── requirements.txt
├── Procfile
├── instance/
├── static/
│   ├── styles.scss
│   └── styles.css
└── templates/
    ├── base.html
    ├── index.html
    └── update.html
```

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Environment Variables
- `PORT` (optional): Port to run the app on. Defaults to `5000`.

## Notes
- The database file is created at `instance/mydatabase.db` automatically on first run.
