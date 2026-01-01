# Product Requirements Document (PRD)

## Project: Open Knesset – Backend API Revamp

---

## 1. Project Overview

### 1.1 Summary
This project is a comprehensive revamp of the backend API for the **Open Knesset** platform. Its goal is to make Israeli parliamentary data more accessible, structured, and usable by providing a modern, developer-friendly REST API.

The backend serves as a data access layer between a PostgreSQL database containing official Knesset data and a separately developed frontend application. The API is designed first and foremost to support the official frontend, while remaining open and useful to external developers, journalists, and researchers.

---

### 1.2 Problem Statement
Although Israeli parliamentary data is publicly available, it is difficult to consume directly due to:

- Highly normalized and fragmented database schemas  
- Queries that require joining many tables to answer common questions  
- Legacy backend patterns that are not optimized for modern frontend development  

As a result, frontend development is slower and more complex than necessary, and external reuse of the data is limited.

---

### 1.3 Value Proposition
The revamped backend API:

- Abstracts complex SQL logic behind clear REST endpoints  
- Provides frontend-ready JSON responses  
- Improves developer experience and maintainability  
- Preserves full historical parliamentary data across all Knesset terms  
- Lowers the barrier for civic-tech reuse of Knesset data  

**Primary value:** High-quality API usability and seamless frontend adoption  
**Secondary value:** A stable, open API for external developers

---

### 1.4 Guiding Principles

- **API-first:** Designed around consumer needs, not database structure  
- **Transparency:** Data reflects official Knesset sources without interpretation  
- **Simplicity:** Favor clarity over cleverness  
- **Best-effort accuracy:** No editorial or legal guarantees  

---

## 2. Technical Requirements

### 2.1 Backend Responsibilities (Explicit Scope)

The backend is intentionally simple and focused. It:

1. Connects to a **PostgreSQL database** containing processed official Knesset data  
2. Executes predefined **SQL queries** (located in `api/queries.py`)  
3. Converts query results into structured **JSON responses**  
4. Serves those responses via **FastAPI REST endpoints**

Anything outside this flow is considered out of scope.

---

### 2.2 Required Technical Expertise

- Python backend development  
- REST API design  
- SQL and relational data modeling  
- Working with large, normalized datasets  
- Docker-based application development  

---

### 2.3 Technology Stack

**Core Stack**

- **Language:** Python 3.10+  
- **Web Framework:** FastAPI  
- **Database:** PostgreSQL  
- **Query Layer:** Raw SQL (explicitly defined and maintained)  
- **Application Server:** Uvicorn  
- **Containerization:** Docker  
- **Configuration:** Environment variables (`.env`)  

**Out of Scope**

- CI/CD pipelines  
- Infrastructure provisioning  
- Monitoring, logging, or analytics systems  
- Authentication systems  

---

### 2.4 Data Sources

- Source of truth: **Official Knesset data**, already ingested into PostgreSQL  
- The backend does not fetch data directly from the Knesset API  
- All historical Knesset terms are supported  

---

## 3. Key Features (Prioritized)

### P0 – Core Features

#### 3.1 Frontend-Oriented REST API

- Clear, predictable REST endpoints  
- JSON responses shaped for direct frontend consumption  
- Stable response formats  

**Impact:** Reduces frontend complexity and accelerates feature delivery

---

#### 3.2 SQL Abstraction Layer

- Complex joins handled internally via curated SQL queries  
- No exposure of raw database schema to API consumers  

**Impact:** Shields consumers from database complexity

---

#### 3.3 Historical Data Coverage

- Uniform access to data across all Knesset terms  
- Consistent API behavior regardless of time period  

**Impact:** Enables longitudinal analysis and comparisons

---

#### 3.4 Open Access with Rate Limiting

- No authentication required  
- Rate limiting to protect availability and prevent abuse  

**Impact:** Supports openness while maintaining system stability

---

### P1 – Important Enhancements

#### 3.5 Reuse and Improvement of Legacy Endpoints

- Preserve well-designed endpoints from the original Open Knesset project  
- Improve naming, consistency, and structure where needed  

**Impact:** Reduces risk and preserves institutional knowledge

---

#### 3.6 Consistent Error Handling

- Standard HTTP status codes  
- Clear, structured error responses  

**Impact:** Improves developer experience and debugging

---

### P2 – Future-Oriented (Non-Blocking)

#### 3.7 External Developer Usability

- Intuitive endpoint naming  
- Predictable data structures  
- Reasonable defaults  

**Impact:** Encourages third-party reuse without increasing core complexity

---

#### 3.8 API Versioning (Deferred)

- Not required initially  
- API design should not prevent future versioning  

**Impact:** Preserves long-term flexibility

---

## 4. Design & Visual Identity (API Perspective)

Although this is a backend project, design principles apply to API structure and developer experience.

### 4.1 API Design Language

- Minimalist and consistent  
- Human-readable field names  
- Shallow nesting where possible  
- Consistent conventions across endpoints  

---

### 4.2 Conceptual Identity

- **Values:** Transparency, neutrality, civic trust  
- **Tone:** Factual and descriptive  
- **Language:** Data is primarily in Hebrew; API structure remains language-agnostic  

---

### 4.3 Documentation Expectations

- Example-driven  
- Focused on real frontend use cases  
- Avoids internal implementation details  

---

## 5. Milestones (Logical Phases)

> No calendar-based schedule is defined due to volunteer-based development.

### Phase 1 – Core Infrastructure

- Application scaffolding  
- Database connectivity  
- Base FastAPI setup  
- Environment configuration  

---

### Phase 2 – Core Endpoints

- Implement endpoints required by the frontend  
- Translate existing SQL logic into stable API responses  
- Validate historical data behavior  

---

### Phase 3 – API Refinement

- Improve consistency and error handling  
- Apply rate limiting  
- Refactor for clarity and reuse  

---

### Phase 4 – Stabilization & Public Readiness

- Frontend feedback-driven improvements  
- Performance tuning where necessary  
- Documentation polish  

---

## Explicit Non-Goals

- Authentication and user management  
- Admin interfaces  
- Real-time or streaming data  
- Editorial analysis or interpretation  
- Infrastructure automation  

