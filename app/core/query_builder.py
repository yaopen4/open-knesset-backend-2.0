import logging
from typing import List, Dict, Union

from fastapi import responses

from app.core.database import get_db_cursor
from app.core.serialization import json_serialize
from app.core.streaming import streaming_response_iterator, ITTER_SIZE

logger = logging.getLogger(__name__)


def get_data_list(
        start_query: str,
        limit: int,
        offset: int,
        order_by: str,
        qs: str):
    """Retrieve a list of data from the database based on the provided parameters."""
    if limit > 10000:
        return ValueError("Can't use limit value above 10000")
    elif limit < 1:
        return ValueError("Can't use limit value under 1")
    result = create_query_list(start_query, limit, offset, order_by, qs)
    if isinstance(result, ValueError):
        return result
    query = result[0]
    values = result[1]
    try:
        if (limit <= ITTER_SIZE):
            with get_db_cursor() as cur:
                cur.execute(query, tuple(values))
                data = cur.fetchall()
                data = json_serialize(data)
                return responses.JSONResponse(content=data)
        else:
            return responses.StreamingResponse(
                streaming_response_iterator(query, values),
                media_type="application/json"
            )
    except Exception as e:
        logger.critical("critical error", e)


def create_query_list(
    start_query: str, limit: int, offset: int,
    order_by=None, qs: str | None = None
):
    """Create a parameterized SQL query and a list of values."""
    where_optional_args = []
    other_optional_args = []
    values = []
    crc32c = False
    
    if qs:
        qs = qs.split('&')
        for item in qs:
            if item[-2:] == '==':
                item = item[:-2]
                crc32c = True
            key, val = item.split('=')
            if crc32c:
                val += '=='
                crc32c = False
            if '[' in val:
                val_splited = val[1:-1].split(',')
                try:
                    val = [int(element) for element in val_splited]
                    val = str(val)
                except Exception:
                    val = str(val).replace("'", '"')
                val = val.replace('\\\\', '\\')
                values.append(val)
                where_optional_args.append('"{0}" @> %s'.format(key))
            elif '<' in val:
                key_splited = key.split('_')
                object_key = key_splited[0]
                if len(key_splited) == 3:
                    object_field = '{0}_{1}'.format(key_splited[1], key_splited[2])
                else:
                    object_field = key_splited[1]
                if not (val[1:-1].isdigit()):
                    val = '[{{"{0}": "{1}"}}]'.format(object_field, val[1:-1])
                else:
                    val = '[{{"{0}": {1}}}]'.format(object_field, val[1:-1])
                values.append(val)
                where_optional_args.append('"{0}" @> %s'.format(object_key))
            else:
                where_optional_args.append('"{0}" = %s'.format(key))
                values.append(val)

    if not where_optional_args:
        where_optional_args.append("1 = 1")

    if order_by is not None:
        other_optional_args.append(f" ORDER BY {order_by}")
    if limit > 0:
        other_optional_args.append(" LIMIT %s")
        values.append(int(limit))
    if offset > 0:
        other_optional_args.append(" OFFSET %s")
        values.append(int(offset))

    if (qs):
        query = (
            f"{start_query} WHERE "
            + " AND ".join(where_optional_args)
            + "".join(other_optional_args)
        )
    else:
        query = (f"{start_query}" + "".join(other_optional_args))
    return [query, values]


def get_single_data(table: str, field: str, value: int):
    """Retrieve a single record from the specified database table."""
    sql = f'select * from {table} where "{field}"={value}'
    try:
        with get_db_cursor() as cur:
            cur.execute(sql)
            data = cur.fetchone()
            if data is None:
                return TypeError('No such data exists! Please enter another ID')
    except Exception as e:
        logger.critical("critical error", e)
    return data

