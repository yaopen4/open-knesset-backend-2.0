# Contributing to Open Knesset Backend

Thank you for your interest in contributing to the Open Knesset Backend! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Making Changes](#making-changes)
- [Code Style Guidelines](#code-style-guidelines)
- [API Design Principles](#api-design-principles)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Documentation](#documentation)
- [Questions and Support](#questions-and-support)

## Code of Conduct

This project is part of the civic-tech community and aims to make Israeli parliamentary data more accessible. We expect all contributors to:

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for all contributors

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- **Python 3.10+** installed
- **PostgreSQL** database access (or a test database)
- **Git** for version control
- Basic familiarity with:
  - Python backend development
  - REST API design
  - SQL and relational databases
  - FastAPI framework

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/open-knesset-backend.git
   cd open-knesset-backend
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/ORIGINAL_OWNER/open-knesset-backend.git
   ```

## Development Setup

### 1. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root with your database credentials:

```env
OKNESSET_DB_USER="your_username"
OKNESSET_DB_PASSWORD="your_password"
OKNESSET_DB_HOST="your_host"
OKNESSET_DB_PORT="5432"
OKNESSET_DB_NAME="postgres"
```

**Note:** For local development, you may need access to a test database. Contact the maintainers if you need help setting one up.

### 4. Run the Development Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. FastAPI automatically provides interactive API documentation at `http://localhost:8000/docs`.

### 5. Using Docker (Optional)

If you prefer to run the application in Docker:

```bash
# Build the image
docker build -t open-knesset-backend .

# Run the container
docker run --env-file .env -p 8000:80 open-knesset-backend
```

## Project Structure

Understanding the project structure will help you navigate the codebase:

```
open-knesset-backend/
├── api/                    # Database and query logic
│   ├── config.py          # API configuration
│   ├── db.py              # Database connection and query execution
│   ├── queries.py         # SQL queries (centralized)
│   └── table_names.py     # Database table name constants
├── models/                 # Pydantic models for data structures
│   ├── bills.py
│   ├── committees.py
│   ├── members.py
│   ├── people.py
│   ├── user_friendly.py   # Frontend-oriented models
│   └── ...
├── docs/                   # Documentation
│   ├── PRD.md             # Product Requirements Document
│   └── CONTRIBUTING.md    # This file
├── main.py                 # FastAPI application and endpoints
├── config.py              # Application settings
├── errors.py              # Error handling utilities
├── requirements.txt       # Python dependencies
└── Dockerfile             # Docker configuration
```

### Key Concepts

- **API-first design:** Endpoints are designed for frontend consumption, not database structure
- **SQL abstraction:** Complex queries live in `api/queries.py` to shield consumers from database complexity
- **Model separation:** Pydantic models in `models/` define API response structures
- **User-friendly models:** The `user_friendly.py` module contains frontend-optimized data structures

## Making Changes

### Before You Start

1. **Check existing issues:** Look for open issues that match what you want to work on
2. **Create an issue:** If you're planning a significant change, consider opening an issue first to discuss
3. **Update your fork:** Keep your fork up to date:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

### Creating a Branch

Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Use descriptive branch names:
- `feature/add-bill-search-endpoint`
- `fix/member-query-performance`
- `docs/update-api-documentation`

## Code Style Guidelines

### Python Style

- Follow **PEP 8** style guidelines
- Use meaningful variable and function names
- Keep functions focused and single-purpose
- Add docstrings for functions and classes

### FastAPI Endpoints

When creating or modifying endpoints:

1. **Use descriptive endpoint paths:**
   ```python
   # Good
   @app.get("/members/{mk_individual_id}")
   
   # Avoid
   @app.get("/m/{id}")
   ```

2. **Include comprehensive docstrings:**
   ```python
   @app.get("/members", 
            status_code=200,
            description="Detailed description of what this endpoint does...",
            summary="Brief summary",
            response_model=List[user_friendly.Member],
            tags=['user friendly'])
   ```

3. **Use appropriate HTTP status codes:**
   - `200` for successful GET requests
   - `201` for successful POST requests
   - `404` for not found
   - `422` for validation errors
   - `500` for server errors

4. **Handle errors consistently:**
   ```python
   if isinstance(data, Exception):
       raise HTTPException(
           status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
           detail={
               'error': type(data).__name__,
               'msg': str(data)
           }
       )
   ```

### SQL Queries

- **Centralize queries:** All SQL queries should be in `api/queries.py`
- **Use parameterized queries:** Always use parameterized queries to prevent SQL injection
- **Add comments:** Document complex queries with comments explaining the logic
- **Follow naming conventions:** Use descriptive function names like `get_member()` or `get_committee_bills()`

### Model Definitions

- Use **Pydantic models** for request/response validation
- Keep models in appropriate files within the `models/` directory
- Use `user_friendly.py` for frontend-optimized response models
- Include field descriptions where helpful

## API Design Principles

When designing new endpoints, follow these principles:

1. **API-first:** Design for consumer needs, not database structure
2. **Consistency:** Follow existing endpoint patterns and naming conventions
3. **Simplicity:** Favor clarity over cleverness
4. **Transparency:** Data should reflect official Knesset sources without interpretation
5. **Frontend-ready:** JSON responses should be structured for direct frontend consumption

### Example: Adding a New Endpoint

1. **Define the SQL query** in `api/queries.py`:
   ```python
   def get_committee_members():
       return """
           SELECT ...
           FROM ...
           WHERE ...
       """
   ```

2. **Create or update models** in `models/` if needed:
   ```python
   class CommitteeMember(BaseModel):
       id: int
       name: str
       # ...
   ```

3. **Add the endpoint** in `main.py`:
   ```python
   @app.get("/committees/{committee_id}/members",
            response_model=List[CommitteeMember],
            tags=['committees'])
   async def get_committee_members(committee_id: int):
       query = QUERY.get_committee_members()
       data = DB.execute_query(query, committee_id)
       if isinstance(data, Exception):
           raise HTTPException(...)
       return data
   ```

## Testing

### Manual Testing

1. **Use FastAPI's interactive docs:** Visit `http://localhost:8000/docs` to test endpoints
2. **Test edge cases:** Try invalid parameters, missing data, etc.
3. **Test across Knesset terms:** Ensure endpoints work for different historical periods
4. **Verify response structure:** Check that responses match the defined models

### Testing Checklist

Before submitting your changes:

- [ ] All endpoints return expected data structures
- [ ] Error handling works correctly
- [ ] Edge cases are handled (missing data, invalid IDs, etc.)
- [ ] Response models match the actual responses
- [ ] Code follows project style guidelines
- [ ] No hardcoded values or credentials

## Submitting Changes

### Commit Messages

Write clear, descriptive commit messages:

```
feat: add endpoint for searching bills by keyword

- Added GET /bills/search endpoint
- Implemented keyword search in SQL query
- Added response model for search results
```

Use conventional commit prefixes:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `perf:` for performance improvements
- `test:` for adding tests

### Pull Request Process

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub with:
   - **Clear title:** Describe what the PR does
   - **Description:** Explain the changes and why they're needed
   - **Reference issues:** Link to related issues (e.g., "Fixes #123")
   - **Screenshots/Examples:** If applicable, include examples of API responses

3. **PR Checklist:**
   - [ ] Code follows style guidelines
   - [ ] Changes are tested locally
   - [ ] Documentation is updated if needed
   - [ ] Commit messages are clear
   - [ ] No merge conflicts with main branch

4. **Respond to feedback:** Be open to suggestions and make requested changes

### Review Process

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## Documentation

### Updating Documentation

- **API Documentation:** FastAPI auto-generates docs from docstrings, so keep them up to date
- **README.md:** Update if you change setup instructions or add new features
- **PRD.md:** For significant feature additions, consider updating the Product Requirements Document

### Code Comments

- Add comments for complex logic or non-obvious decisions
- Document SQL queries that involve multiple joins or complex logic
- Explain why something is done a certain way, not just what it does

## Questions and Support

### Getting Help

- **Open an issue:** For bugs, feature requests, or questions
- **Check existing issues:** Your question might already be answered
- **Review the PRD:** See `docs/PRD.md` for project goals and design principles

### Communication

- Be respectful and constructive in all communications
- Provide context when asking questions
- Help others when you can

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

Thank you for contributing to Open Knesset Backend! Your efforts help make Israeli parliamentary data more accessible to everyone.

