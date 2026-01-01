from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import plenum
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['plenum'])


@router.get("/plenum_kns_documentplenumsession/list",
            status_code=200,
            response_model=List[plenum.DocumentPlenumSession],
            responses={422: errors.LIMIT_ERROR})
async def get_documentplenumsession_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    PlenumSessionID: Optional[int] = None,
    GroupTypeID: Optional[int] = None,
    GroupTypeDesc: Optional[str] = None,
    ApplicationID: Optional[int] = None,
    ApplicationDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list plenum_kns_documentplenumsession table"""
    query_params = request.query_params.items()
    order_by = '"DocumentPlenumSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM plenum_kns_documentplenumsession"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/plenum_kns_documentplenumsession/{DocumentPlenumSessionID}',
            response_model=plenum.DocumentPlenumSession,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_documentplenumsession(DocumentPlenumSessionID: int):
    """Route for single plenum_kns_documentplenumsession table"""
    data = DB.get_single_data('plenum_kns_documentplenumsession', 'DocumentPlenumSessionID', DocumentPlenumSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/plenum_kns_plenumsession/list",
            status_code=200,
            response_model=List[plenum.PlenumSession],
            responses={422: errors.LIMIT_ERROR})
async def get_plenumsession_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Number: Optional[int] = None,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    StartDate: Optional[datetime] = None,
    FinishDate: Optional[datetime] = None,
    IsSpecialMeeting: Optional[bool] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list plenum_kns_plenumsession table"""
    query_params = request.query_params.items()
    order_by = '"PlenumSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM plenum_kns_plenumsession"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/plenum_kns_plenumsession/{PlenumSessionID}',
            response_model=plenum.PlenumSession,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_plenumsession(PlenumSessionID: int):
    """Route for single plenum_kns_plenumsession table"""
    data = DB.get_single_data('plenum_kns_plenumsession', 'PlenumSessionID', PlenumSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/plenum_kns_plmsessionitem/list",
            status_code=200,
            response_model=List[plenum.PlmSessionItem],
            responses={422: errors.LIMIT_ERROR})
async def get_plmsessionitem_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    PlenumSessionID: Optional[int] = None,
    ItemTypeID: Optional[int] = None,
    ItemTypeDesc: Optional[str] = None,
    Ordinal: Optional[int] = None,
    Name: Optional[str] = None,
    StatusID: Optional[int] = None,
    IsDiscussion: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list plenum_kns_plmsessionitem table"""
    query_params = request.query_params.items()
    order_by = '"ItemID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM plenum_kns_plmsessionitem"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/plenum_kns_plmsessionitem/{ItemID}',
            response_model=plenum.PlmSessionItem,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_plmsessionitem(ItemID: int):
    """Route for single plenum_kns_plmsessionitem table"""
    data = DB.get_single_data('plenum_kns_plmsessionitem', 'ItemID', ItemID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

