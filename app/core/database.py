from functools import lru_cache
from contextlib import contextmanager
import logging

import psycopg2
from psycopg2.extras import RealDictCursor

from app import config

logger = logging.getLogger(__name__)


@lru_cache
def get_settings():
    return config.Settings()


def get_db_connection(settings=None):
    if settings is None:
        settings = get_settings()
    return psycopg2.connect(
        host=settings.oknesset_db_host,
        port=settings.oknesset_db_port,
        database=settings.oknesset_db_name,
        user=settings.oknesset_db_user,
        password=settings.oknesset_db_password,
    )


@contextmanager
def get_db_cursor(cursor_name: str = 'oknesset'):
    conn = get_db_connection()
    if cursor_name:
        cur = conn.cursor(name=cursor_name, cursor_factory=RealDictCursor)
    else:
        cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cur
    finally:
        cur.close()
        conn.close()


def is_mk_individual_exist(mk_individual_id: int):
    try:
        with get_db_cursor() as cur:
            cur.execute("""SELECT mk_individual_id
                            FROM members_mk_individual
                            WHERE mk_individual_id=%s""",
                        (mk_individual_id,))
            is_member_exist = cur.fetchone()
            if is_member_exist is None:
                return False
            return True
    except Exception as e:
        logger.critical("critical error", e)


def is_knesset_term_exist(knesset_term: int):
    try:
        with get_db_cursor() as cur:
            cur.execute("""SELECT "KnessetNum"
                            FROM knesset_kns_knessetdates
                            WHERE "KnessetNum"=%s""",
                        (knesset_term,))
            is_term_exist = cur.fetchone()
            if is_term_exist is None:
                return False
            return True
    except Exception as e:
        logger.critical("critical error", e)

