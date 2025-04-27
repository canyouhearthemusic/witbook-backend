# Witbook Backend

[![CI](https://github.com/canyouhearthemusic/witbook-backend/actions/workflows/ci.yml/badge.svg)](https://github.com/canyouhearthemusic/witbook-backend/actions/workflows/ci.yml)
[![CD](https://github.com/canyouhearthemusic/witbook-backend/actions/workflows/cd.yml/badge.svg)](https://github.com/canyouhearthemusic/witbook-backend/actions/workflows/cd.yml)

A Django-based backend for a book tracking application with features for managing reading sessions, book collections, and user profiles.

## Features

- User authentication and profile management
- Book tracking and management
- Reading session tracking with notes
- RESTful API using Django REST Framework
- JWT-based authentication

## Technology Stack

- Python 3.11
- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions for CI/CD

## Development Setup

### Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/canyouhearthemusic/witbook-backend.git
   cd witbook-backend
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the provided example:
   ```
   cp .env.example .env
   ```

4. Run with Docker Compose:
   ```
   docker-compose up -d
   ```

5. Or run locally (requires PostgreSQL running):
   ```
   python manage.py migrate
   python manage.py runserver
   ```

### Testing

Run tests with pytest:
```
pytest
```

Run with coverage:
```
pytest --cov=./ --cov-report=term
```

### Linting and Formatting

Format code with Black and isort using the custom command:
```
python manage.py format_code
```

Or manually:
```
black .
isort --profile black .
```

Lint with flake8:
```
flake8
```

## API Documentation

API documentation is available at `/swagger/` when the server is running.

## Environment Variables

The following environment variables can be set in the `.env` file:

- `DEBUG`: Set to "True" for development, "False" for production
- `SECRET_KEY`: Django secret key
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `POSTGRES_DB`: PostgreSQL database name
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_HOST`: PostgreSQL host
- `POSTGRES_PORT`: PostgreSQL port

## Deployment

The project includes CI/CD configuration with GitHub Actions:

1. CI workflow: Runs linting and tests on all branches
2. CD workflow: Builds and pushes a Docker image to Docker Hub on main branch and tags

## Project Structure

```
witbook-backend/
├── .github/              # GitHub Actions workflows
├── books/                # Books app
├── media/                # User-uploaded media
├── scripts/              # Utility scripts
├── users/                # Users app
├── witbook/              # Project settings
├── .env                  # Environment variables
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
├── manage.py             # Django management script
├── pytest.ini            # Pytest configuration
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Create a new Pull Request 