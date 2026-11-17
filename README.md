# Unfinished Business API

A Flask backend for the [Unfinished-Business-Web](https://github.com/beekeeperkeepbee-maker/Unfinished-Business-Web) app.

## Endpoints

- `GET /projects` — List all projects (unfinished and finished)
- `POST /projects` — Add a new project (body: `{"name": "..."}`)
- `POST /projects/finish/<index>` — Move a project to the finished list
- `POST /projects/delete/<index>` — Delete a project

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

The server runs on http://localhost:5000.

## Status

- [x] Backend is deployed and live on Render.
- [x] Frontend is connected and communicating with the API.
- [x] Connected to a **Supabase PostgreSQL database** for permanent storage.
- [x] Keep-alive monitor (UptimeRobot) prevents free-tier cold starts.

## Roadmap

- [x] Version 1.0 — Flask server with CRUD endpoints
- [x] Version 1.1 — Deploy to a public host (Render)
- [x] Version 1.2 — Connect the web frontend to the API
- [x] Version 1.3 — Migrate local JSON storage to Supabase PostgreSQL database

## Database

This API uses a Supabase PostgreSQL database. The `DATABASE_URL` environment variable on Render holds the connection string. The database table is created with the following schema:

```sql
create table projects (
  id bigint primary key generated always as identity,
  name text not null,
  status text not null default 'unfinished'
);
