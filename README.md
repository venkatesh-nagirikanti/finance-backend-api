# Finance Backend API

A simple Finance Management Backend built using FastAPI and SQLAlchemy.

## Features
- Create users
- Add income and expense records
- Filter records (income / expense)
- Dashboard summary (total income, total expense, balance)
- Role-based access (Admin / Viewer)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite

## Project Structure
main.py – Entry point
models/ – Database models
routes/ – API routes
database/ – Database connection

## Run the Project
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

## API Endpoints
POST /users – Create user
GET /users – Get users
POST /records – Create record
GET /records – Get records
GET /dashboard – Get summary

Author
Venkatesh N
