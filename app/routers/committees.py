from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import committees
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['committees'])


@router.get("/committees_kns_documentcommitteesession_dataservice/list",
            status_code=200,
            response_model=List[committees.KnsDocumentCommitteeSessionDataservice],
            responses={422: errors.LIMIT_ERROR})
async def get_documentcommitteesession_dataservice_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    CommitteeSessionID: Optional[int] = None,
    GroupTypeID: Optional[int] = None,
    GroupTypeDesc: Optional[str] = None,
    ApplicationID: Optional[int] = None,
    ApplicationDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list committees_kns_documentcommitteesession_dataservice table"""
    query_params = request.query_params.items()
    order_by = '"DocumentCommitteeSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM committees_kns_documentcommitteesession_dataservice"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/committees_kns_documentcommitteesession_dataservice/{DocumentCommitteeSessionID}',
            response_model=committees.KnsDocumentCommitteeSessionDataservice,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_documentcommitteesession_dataservice(DocumentCommitteeSessionID: int):
    """Route for single committees_kns_documentcommitteesession_dataservice table"""
    data = DB.get_single_data('committees_kns_documentcommitteesession_dataservice', 'DocumentCommitteeSessionID', DocumentCommitteeSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/committees_kns_jointcommittee/list",
            status_code=200,
            response_model=List[committees.KnsJointCommittee],
            responses={422: errors.LIMIT_ERROR})
async def get_jointcommittee_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    CommitteeID: Optional[int] = None,
    ParticipantCommitteeID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list committees_kns_jointcommittee table"""
    query_params = request.query_params.items()
    order_by = '"JointCommitteeID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM committees_kns_jointcommittee"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/committees_kns_jointcommittee/{JointCommitteeID}',
            response_model=committees.KnsJointCommittee,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_jointcommittee(JointCommitteeID: int):
    """Route for single committees_kns_jointcommittee table"""
    data = DB.get_single_data('committees_kns_jointcommittee', 'JointCommitteeID', JointCommitteeID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/committees_kns_committee/list",
            status_code=200,
            response_model=List[committees.KnsCommittee],
            responses={422: errors.LIMIT_ERROR})
async def get_committee_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Name: Optional[str] = None,
    CategoryID: Optional[int] = None,
    CategoryDesc: Optional[str] = None,
    KnessetNum: Optional[int] = None,
    CommitteeTypeID: Optional[int] = None,
    CommitteeTypeDesc: Optional[str] = None,
    IsCurrent: Optional[bool] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list committees_kns_committee table"""
    query_params = request.query_params.items()
    order_by = '"CommitteeID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM committees_kns_committee"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/committees_kns_committee/{CommitteeID}',
            response_model=committees.KnsCommittee,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_committee(CommitteeID: int):
    """Route for single committees_kns_committee table"""
    data = DB.get_single_data('committees_kns_committee', 'CommitteeID', CommitteeID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/committees_kns_committeesession/list",
            status_code=200,
            response_model=List[committees.KnsCommitteeSession],
            responses={422: errors.LIMIT_ERROR})
async def get_committeesession_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    Number: Optional[int] = None,
    KnessetNum: Optional[int] = None,
    TypeID: Optional[int] = None,
    TypeDesc: Optional[str] = None,
    CommitteeID: Optional[int] = None,
    StartDate: Optional[datetime] = None,
    FinishDate: Optional[datetime] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list committees_kns_committeesession table"""
    query_params = request.query_params.items()
    order_by = '"CommitteeSessionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM committees_kns_committeesession"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/committees_kns_committeesession/{CommitteeSessionID}',
            response_model=committees.KnsCommitteeSession,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_committeesession(CommitteeSessionID: int):
    """Route for single committees_kns_committeesession table"""
    data = DB.get_single_data('committees_kns_committeesession', 'CommitteeSessionID', CommitteeSessionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

