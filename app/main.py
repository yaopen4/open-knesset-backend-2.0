"""
Open Knesset Backend API

This is the main FastAPI application entry point.
All routes are organized into domain-specific routers.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    members,
    bills,
    votes,
    committees,
    plenum,
    knesset,
    laws,
    lobbyists,
    people,
)

app = FastAPI(
    title="Open Knesset API",
    description="REST API for the Israeli Knesset data",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['*']
)

# Include all routers
app.include_router(members.router)
app.include_router(bills.router)
app.include_router(votes.router)
app.include_router(committees.router)
app.include_router(plenum.router)
app.include_router(knesset.router)
app.include_router(laws.router)
app.include_router(lobbyists.router)
app.include_router(people.router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint returning API info."""
    return {
        "message": "Open Knesset API",
        "docs": "/docs",
        "version": "1.0.0"
    }

