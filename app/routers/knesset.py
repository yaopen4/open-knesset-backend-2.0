from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import knesset
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['knesset'])


@router.get("/knesset_kns_govministry/list",
            status_code=200,
            response_model=List[knesset.KnsGovministry],
            responses={422: errors.LIMIT_ERROR})
async def get_govministry_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Name: Optional[str] = None,
    IsActive: Optional[bool] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list knesset_kns_govministry table"""
    query_params = request.query_params.items()
    order_by = '"GovMinistryID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM knesset_kns_govministry"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/knesset_kns_govministry/{GovMinistryID}',
            response_model=knesset.KnsGovministry,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_govministry(GovMinistryID: int):
    """Route for single knesset_kns_govministry table"""
    data = DB.get_single_data('knesset_kns_govministry', 'GovMinistryID', GovMinistryID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/knesset_kns_knessetdates/list",
            status_code=200,
            response_model=List[knesset.KnsKnessetDates],
            responses={422: errors.LIMIT_ERROR})
async def get_knessetdates_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    Assembly: Optional[int] = None,
    Plenum: Optional[int] = None,
    IsCurrent: Optional[bool] = None,
):
    """Route for list knesset_kns_knessetdates table"""
    query_params = request.query_params.items()
    order_by = '"KnessetDateID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM knesset_kns_knessetdates"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/knesset_kns_knessetdates/{KnessetDateID}',
            response_model=knesset.KnsKnessetDates,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_knessetdates(KnessetDateID: int):
    """Route for single knesset_kns_knessetdates table"""
    data = DB.get_single_data('knesset_kns_knessetdates', 'KnessetDateID', KnessetDateID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/knesset_kns_status/list",
            status_code=200,
            response_model=List[knesset.KnsStatus],
            responses={422: errors.LIMIT_ERROR})
async def get_status_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Desc: Optional[str] = None,
    TypeID: Optional[int] = None,
    TypeDesc: Optional[str] = None,
    IsActive: Optional[bool] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list knesset_kns_status table"""
    query_params = request.query_params.items()
    order_by = '"StatusID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM knesset_kns_status"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/knesset_kns_status/{StatusID}',
            response_model=knesset.KnsStatus,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_status(StatusID: int):
    """Route for single knesset_kns_status table"""
    data = DB.get_single_data('knesset_kns_status', 'StatusID', StatusID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/knesset_kns_itemtype/list",
            status_code=200,
            response_model=List[knesset.KnsItemtype],
            responses={422: errors.LIMIT_ERROR})
async def get_itemtype_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Desc: Optional[str] = None,
    TableName: Optional[str] = None,
):
    """Route for list knesset_kns_itemtype table"""
    query_params = request.query_params.items()
    order_by = '"ItemTypeID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM knesset_kns_itemtype"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/knesset_kns_itemtype/{ItemTypeID}',
            response_model=knesset.KnsItemtype,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_itemtype(ItemTypeID: int):
    """Route for single knesset_kns_itemtype table"""
    data = DB.get_single_data('knesset_kns_itemtype', 'ItemTypeID', ItemTypeID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

