from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional

from app.schemas import lobbyists
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['lobbyists'])


@router.get("/lobbyists_v_lobbyist_clients/list",
            status_code=200,
            response_model=List[lobbyists.LobbyistClients],
            responses={422: errors.LIMIT_ERROR})
async def get_lobbyist_clients_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    LobbyistID: Optional[int] = None,
    ClientID: Optional[int] = None,
    Name: Optional[str] = None,
    ClientsNames: Optional[str] = None,
):
    """Route for list lobbyists_v_lobbyist_clients table"""
    query_params = request.query_params.items()
    order_by = '"LobbyistID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM lobbyists_v_lobbyist_clients"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/lobbyists_v_lobbyist/list",
            status_code=200,
            response_model=List[lobbyists.Lobbyist],
            responses={422: errors.LIMIT_ERROR})
async def get_lobbyist_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    LobbyistID: Optional[int] = None,
    IdentityNumber: Optional[str] = None,
    FullName: Optional[str] = None,
    PermitTypeValue: Optional[str] = None,
    CorporationName: Optional[str] = None,
    IsIndependent: Optional[bool] = None,
    MemberInFaction: Optional[bool] = None,
):
    """Route for list lobbyists_v_lobbyist table"""
    query_params = request.query_params.items()
    order_by = '"LobbyistID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM lobbyists_v_lobbyist"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/lobbyists_v_lobbyist/{LobbyistID}',
            response_model=lobbyists.Lobbyist,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_lobbyist(LobbyistID: int):
    """Route for single lobbyists_v_lobbyist table"""
    data = DB.get_single_data('lobbyists_v_lobbyist', 'LobbyistID', LobbyistID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

