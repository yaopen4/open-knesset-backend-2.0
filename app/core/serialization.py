from datetime import datetime, date
from decimal import Decimal
from typing import List, Dict


def json_serialize(data: List[Dict]):
    """Serialize a list of dictionaries to JSON-compatible format."""
    def serialize_value(value):
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S")
        elif isinstance(value, date):
            return value.strftime("%d/%m/%y")
        elif isinstance(value, Decimal):
            return float(value)
        else:
            return value

    return [
        {
            key: serialize_value(value) for key, value in row.items()
        }
        for row in data
    ]

