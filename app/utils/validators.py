# Input validation helpers

def validate_limit(limit: int) -> None:
    """Validate limit parameter is within acceptable range."""
    if limit > 10000:
        raise ValueError("Can't use limit value above 10000")
    if limit < 1:
        raise ValueError("Can't use limit value under 1")


def validate_knesset_term(knesset_term: int) -> bool:
    """Validate knesset term is within valid range (1-current)."""
    return 1 <= knesset_term <= 26


def validate_mk_individual_id(mk_individual_id: int) -> bool:
    """Validate mk_individual_id is positive."""
    return mk_individual_id > 0

