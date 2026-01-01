import json
import logging

from fastapi import encoders
from app.core.database import get_db_cursor

logger = logging.getLogger(__name__)
ITTER_SIZE = 500


def streaming_response_iterator(query: str, values):
    """Stream data from the database as a JSON array."""
    try:
        yield b"["
        with get_db_cursor() as cur:
            cur.itersize = ITTER_SIZE
            cur.execute(query, tuple(values))
            for i, obj in enumerate(cur):
                item = encoders.jsonable_encoder(obj)
                if i > 0:
                    yield b","
                yield json.dumps(item).encode()
            yield b"]"
    except Exception as e:
        logger.critical("critical error 500", e)

