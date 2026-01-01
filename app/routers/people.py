from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import people
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['people'])


@router.get("/people_plenum_session_voters_stats/list",
            status_code=200,
            response_model=List[people.PlenumSessionVotersStats],
            responses={422: errors.LIMIT_ERROR})
async def get_plenum_session_voters_stats_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    knesset: Optional[int] = None,
    plenum: Optional[int] = None,
    assembly: Optional[int] = None,
    faction_id: Optional[int] = None,
    mk_id: Optional[int] = None,
):
    """Route for list people_plenum_session_voters_stats table"""
    query_params = request.query_params.items()
    order_by = 'knesset desc, mk_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM people_plenum_session_voters_stats"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/people_committees_joined_meetings/list",
            status_code=200,
            response_model=List[people.CommitteesJoinedMeetings],
            responses={422: errors.LIMIT_ERROR})
async def get_committees_joined_meetings_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    CommitteeSessionID: Optional[int] = None,
    KnessetNum: Optional[int] = None,
    CommitteeID: Optional[int] = None,
    TypeID: Optional[int] = None,
):
    """Route for list people_committees_joined_meetings table"""
    query_params = request.query_params.items()
    order_by = '"CommitteeSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM people_committees_joined_meetings"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/people_committees_joined_meetings/{CommitteeSessionID}',
            response_model=people.CommitteesJoinedMeetings,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_committees_joined_meeting(CommitteeSessionID: int):
    """Route for single people_committees_joined_meetings table"""
    data = DB.get_single_data('people_committees_joined_meetings', 'CommitteeSessionID', CommitteeSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/people_committees_meeting_attendees/list",
            status_code=200,
            response_model=List[people.CommitteesMeetingAttendees],
            responses={422: errors.LIMIT_ERROR})
async def get_committees_meeting_attendees_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    CommitteeSessionID: Optional[int] = None,
    KnessetNum: Optional[int] = None,
    CommitteeID: Optional[int] = None,
    TypeID: Optional[int] = None,
):
    """Route for list people_committees_meeting_attendees table"""
    query_params = request.query_params.items()
    order_by = '"CommitteeSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM people_committees_meeting_attendees"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/people_committees_meeting_attendees/{CommitteeSessionID}',
            response_model=people.CommitteesMeetingAttendees,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_committees_meeting_attendee(CommitteeSessionID: int):
    """Route for single people_committees_meeting_attendees table"""
    data = DB.get_single_data('people_committees_meeting_attendees', 'CommitteeSessionID', CommitteeSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/people_mk_party_discipline_stats/list",
            status_code=200,
            response_model=List[people.PartyDisciplineStats],
            responses={422: errors.LIMIT_ERROR})
async def get_mk_party_discipline_stats_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    knesset: Optional[int] = None,
    plenum: Optional[int] = None,
    assembly: Optional[int] = None,
    faction_id: Optional[int] = None,
    mk_id: Optional[int] = None,
):
    """Route for list people_mk_party_discipline_stats table"""
    query_params = request.query_params.items()
    order_by = 'knesset desc, mk_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM people_mk_party_discipline_stats"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/people_members_joined_mks/list",
            status_code=200,
            response_model=List[people.MembersJoinedMks],
            responses={422: errors.LIMIT_ERROR})
async def get_members_joined_mks_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    mk_individual_id: Optional[int] = None,
    PersonID: Optional[int] = None,
    IsCurrent: Optional[bool] = None,
):
    """Route for list people_members_joined_mks table"""
    query_params = request.query_params.items()
    order_by = 'mk_individual_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM people_members_joined_mks"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/people_members_joined_mks/{mk_individual_id}',
            response_model=people.MembersJoinedMks,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_members_joined_mk(mk_individual_id: int):
    """Route for single people_members_joined_mks table"""
    data = DB.get_single_data('people_members_joined_mks', 'mk_individual_id', mk_individual_id)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

