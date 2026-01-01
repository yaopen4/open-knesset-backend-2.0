from typing_extensions import Annotated
from fastapi import Depends

from app.core.database import get_settings, get_db_cursor

# Re-export for convenience
__all__ = ['get_settings', 'get_db_cursor', 'Annotated', 'Depends']

