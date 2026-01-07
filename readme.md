# Simple Access Control Log API

This project is a Django-based RESTful API for logging door access events, simulating a small part of an access control ecosystem. It uses Django Rest Framework (DRF) to implement CRUD operations on access logs, integrates Django signals for external logging via system commands, and follows Git best practices.

## Features

- **Data Model**: `AccessLog` model with fields:
  - `card_id` (e.g., "C1001")
  - `door_name` (e.g., "Main Entrance")
  - `access_granted` (True/False)
  - `timestamp` (auto-set on creation)
- **API Endpoints**:
  - `POST /api/logs/` – Create a new access log entry
  - `GET /api/logs/` – List all access log entries (with optional filtering)
  - `GET /api/logs/<id>/` – Retrieve a single entry
  - `PUT /api/logs/<id>/` – Update an entry (timestamp not updatable)
  - `DELETE /api/logs/<id>/` – Delete an entry
- **Signals Integration**:
  - On create: Appends event to `system_events.log` using `subprocess`
  - On delete: Appends deletion event to `system_events.log`
- **Git Practices**:
  - Developed on a `development` branch
  - Merged into `main` with clean history
  - Includes proper `.gitignore`
- **Bonus Features Implemented**:
  - Unit tests for API endpoints
  - Filtering on list endpoint (e.g., `?card_id=C1001`)
  - Containerized with Docker

## Requirements

- Python 3.8+
- Django 4.2+
- Django Rest Framework
- SQLite3 (default)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheReinforce43/sicuten-company-project.git
   cd Sicunet_Project



# Create
curl -X POST http://127.0.0.1:8000/api/logs/ \
  -H "Content-Type: application/json" \
  -d '{"card_id": "C1001", "door_name": "Main Entrance", "access_granted": true}'

# List all
curl http://127.0.0.1:8000/api/logs/

# Filter by card_id
curl http://127.0.0.1:8000/api/logs/?card_id=C1001

# Retrieve one
curl http://127.0.0.1:8000/api/logs/1/

# Update
curl -X PUT http://127.0.0.1:8000/api/logs/1/ \
  -H "Content-Type: application/json" \
  -d '{"card_id": "C1002", "door_name": "Side Door", "access_granted": false}'

# Delete
curl -X DELETE http://127.0.0.1:8000/api/logs/1/