from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime, date, time

from app.schemas import votes
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['votes'])


@router.get("/votes_view_vote_rslts_hdr_approved/list",
            status_code=200,
            response_model=List[votes.ViewVoteRsltsHdrApproved],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_rslts_hdr_approved_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    knesset_num: Optional[int] = None,
    session_id: Optional[int] = None,
    vote_item_id: Optional[int] = None,
    vote_date: Optional[date] = None,
    is_accepted: Optional[int] = None,
):
    """Route for list votes_view_vote_rslts_hdr_approved table"""
    query_params = request.query_params.items()
    order_by = 'id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_view_vote_rslts_hdr_approved"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/votes_view_vote_rslts_hdr_approved/{id}',
            response_model=votes.ViewVoteRsltsHdrApproved,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_vote_rslts_hdr_approved(id: int):
    """Route for single votes_view_vote_rslts_hdr_approved table"""
    data = DB.get_single_data('votes_view_vote_rslts_hdr_approved', 'id', id)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/votes_vote_rslts_kmmbr_shadow_extra/list",
            status_code=200,
            response_model=List[votes.VoteRsltsKmmbrShadowExtra],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_rslts_kmmbr_shadow_extra_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    vote_id: Optional[int] = None,
    kmmbr_id: Optional[str] = None,
    knesset_num: Optional[int] = None,
    faction_id: Optional[int] = None,
    mk_individual_id: Optional[int] = None,
):
    """Route for list votes_vote_rslts_kmmbr_shadow_extra table"""
    query_params = request.query_params.items()
    order_by = 'vote_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_vote_rslts_kmmbr_shadow_extra"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/votes_view_vote_mk_individual/list",
            status_code=200,
            response_model=List[votes.ViewVoteMkIndividual],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_mk_individual_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    vip_id: Optional[str] = None,
    mk_individual_id: Optional[int] = None,
):
    """Route for list votes_view_vote_mk_individual table"""
    query_params = request.query_params.items()
    order_by = 'mk_individual_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_view_vote_mk_individual"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/votes_vote_rslts_kmmbr_shadow/list",
            status_code=200,
            response_model=List[votes.VoteRsltsKmmbrShadow],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_rslts_kmmbr_shadow_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    vote_id: Optional[int] = None,
    kmmbr_id: Optional[str] = None,
    knesset_num: Optional[int] = None,
    faction_id: Optional[int] = None,
):
    """Route for list votes_vote_rslts_kmmbr_shadow table"""
    query_params = request.query_params.items()
    order_by = 'vote_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_vote_rslts_kmmbr_shadow"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/votes_view_vote_rslts_hdr_approved_extra/list",
            status_code=200,
            response_model=List[votes.ViewVoteRsltsHdrApprovedExtra],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_rslts_hdr_approved_extra_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    knesset_num: Optional[int] = None,
    session_id: Optional[int] = None,
    vote_item_id: Optional[int] = None,
    vote_date: Optional[date] = None,
    is_accepted: Optional[int] = None,
):
    """Route for list votes_view_vote_rslts_hdr_approved_extra table"""
    query_params = request.query_params.items()
    order_by = 'id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_view_vote_rslts_hdr_approved_extra"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/votes_view_vote_rslts_hdr_approved_extra/{id}',
            response_model=votes.ViewVoteRsltsHdrApprovedExtra,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_vote_rslts_hdr_approved_extra(id: int):
    """Route for single votes_view_vote_rslts_hdr_approved_extra table"""
    data = DB.get_single_data('votes_view_vote_rslts_hdr_approved_extra', 'id', id)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/votes_vote_result_type/list",
            status_code=200,
            response_model=List[votes.VoteResultType],
            responses={422: errors.LIMIT_ERROR})
async def get_vote_result_type_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
):
    """Route for list votes_vote_result_type table"""
    query_params = request.query_params.items()
    order_by = 'result_type_id desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM votes_vote_result_type"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/votes_vote_result_type/{result_type_id}',
            response_model=votes.VoteResultType,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_vote_result_type(result_type_id: int):
    """Route for single votes_vote_result_type table"""
    data = DB.get_single_data('votes_vote_result_type', 'result_type_id', result_type_id)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

