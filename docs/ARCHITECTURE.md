# Architecture

Technical documentation for the Open Knesset Backend API.

## Project Structure

```
open-knesset-backend/
├── app/                          # Modular application structure
│   ├── main.py                   # FastAPI app with router includes
│   ├── config.py                 # Centralized configuration
│   ├── dependencies.py           # Shared dependencies
│   ├── core/                     # Core utilities
│   │   ├── database.py           # DB connection management
│   │   ├── query_builder.py      # Query building utilities
│   │   ├── streaming.py          # Streaming response utilities
│   │   └── serialization.py      # JSON serialization helpers
│   ├── routers/                  # Domain-specific API routes
│   │   ├── members.py            # /members/* endpoints
│   │   ├── bills.py              # /bills_* endpoints
│   │   ├── votes.py              # /votes_* endpoints
│   │   ├── committees.py         # /committees_* endpoints
│   │   ├── plenum.py             # /plenum_* endpoints
│   │   ├── knesset.py            # /knesset_* endpoints
│   │   ├── laws.py               # /laws_* endpoints
│   │   ├── lobbyists.py          # /lobbyists_* endpoints
│   │   └── people.py             # /people_* endpoints
│   ├── queries/                  # SQL queries by domain
│   │   ├── members.py
│   │   ├── bills.py
│   │   └── ...
│   ├── schemas/                  # Pydantic models
│   │   ├── members.py
│   │   ├── bills.py
│   │   └── ...
│   └── utils/                    # Utility modules
│       ├── validators.py
│       └── table_names.py
├── api/                          # Legacy API module (kept for compatibility)
├── models/                       # Legacy models (kept for compatibility)
├── main.py                       # Legacy main (still functional)
├── config.py                     # Root config
├── errors.py                     # Error definitions
├── docs/
├── static/
├── Dockerfile
├── gunicorn_conf.py
├── requirements.txt
└── README.md
```

## API Documentation

Once running, access the interactive API documentation at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Design Decisions

### Domain-Driven Architecture

The codebase follows a domain-driven design where each legislative domain (members, bills, votes, etc.) has its own:
- **Router**: Handles HTTP endpoints
- **Queries**: Contains SQL query definitions
- **Schemas**: Pydantic models for request/response validation

### Core Utilities

- **database.py**: Manages PostgreSQL connections and pooling
- **query_builder.py**: Provides utilities for constructing dynamic SQL queries
- **streaming.py**: Handles streaming large response datasets
- **serialization.py**: Custom JSON serialization for complex types

### Migration Notes

The codebase was reorganized from a monolithic `main.py` (4900+ lines) into a modular, domain-driven architecture. Benefits include:

- **Better maintainability**: Each domain has its own router, queries, and schemas
- **Clearer separation of concerns**: Database logic, query building, and streaming are separated
- **Easier testing**: Modular components can be tested independently
- **Preserved compatibility**: The legacy `main.py` still works during migration

