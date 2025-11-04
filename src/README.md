# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities

## Getting Started

1. Install the dependencies:

   ```
   pip install -r ../requirements.txt
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |

## Data Model

The application uses a simple data model with meaningful identifiers:

1. **Activities** - Uses activity name as identifier:

   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of student emails who are signed up

2. **Students** - Uses email as identifier:
   - Name
   - Grade level

All data is stored in memory, which means data will be reset when the server restarts.

## Security notes (starter)

- This project is starting to collect more sensitive data and to support admin actions. Before adding any admin UI or persisting user credentials, follow these minimal security steps:
   - Store passwords only as salted hashes (use `passlib[bcrypt]` or `argon2-cffi`). A small example helper is provided in `scripts/hash_password_example.py`.
   - Validate incoming request payloads using Pydantic models to avoid malformed input.
   - Prefer token-based auth (JWT) for APIs instead of cookie-based sessions to reduce CSRF surface area; if you use cookies, adopt proper CSRF protections.
   - Avoid raw SQL string interpolation; use parameterized queries or an ORM (SQLAlchemy/SQLModel).

These are starter notes — create a security checklist and complete the audit when moving beyond local development.
