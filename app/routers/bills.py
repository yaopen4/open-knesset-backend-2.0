from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import bills
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['bills'])


@router.get("/bills_kns_billunion/list",
            status_code=200,
            response_model=List[bills.KnsBillUnion],
            responses={422: errors.LIMIT_ERROR})
async def get_billunion_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    MainBillID: Optional[int] = None,
    UnionBillID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list "bills_kns_billunion" table"""
    query_params = request.query_params.items()
    order_by = '"BillUnionID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_billunion"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY
                           if isinstance(data, ValueError)
                           else status.HTTP_404_NOT_FOUND)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get('/bills_kns_billunion/{BillUnionID}',
            response_model=bills.KnsBillUnion,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_union(BillUnionID: int):
    """Route for single "bills_kns_billunion" table"""
    data = DB.get_single_data('bills_kns_billunion', 'BillUnionID', BillUnionID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_billsplit/list",
            status_code=200,
            response_model=List[bills.KnsBillSplit],
            responses={422: errors.LIMIT_ERROR})
async def get_billsplit_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    MainBillID: Optional[int] = None,
    SplitBillID: Optional[int] = None,
    Name: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_billsplit table"""
    query_params = request.query_params.items()
    order_by = '"BillSplitID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_billsplit"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_billsplit/{BillSplitID}',
            response_model=bills.KnsBillSplit,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_split(BillSplitID: int):
    """Route for "bills_kns_billsplit" table"""
    data = DB.get_single_data('bills_kns_billsplit', 'BillSplitID', BillSplitID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_billinitiator/list",
            status_code=200,
            response_model=List[bills.KnsBillInitiator],
            responses={422: errors.LIMIT_ERROR})
async def get_billinitiator_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    BillID: Optional[int] = None,
    PersonID: Optional[int] = None,
    IsInitiator: Optional[bool] = None,
    Ordinal: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_billinitiator table"""
    query_params = request.query_params.items()
    order_by = '"BillInitiatorID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_billinitiator"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_billinitiator/{BillInitiatorID}',
            response_model=bills.KnsBillInitiator,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_initiator(BillInitiatorID: int):
    """Route for single "bills_kns_billinitiator" table"""
    data = DB.get_single_data('bills_kns_billinitiator', 'BillInitiatorID', BillInitiatorID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_billname/list",
            status_code=200,
            response_model=List[bills.KnsBillName],
            responses={422: errors.LIMIT_ERROR})
async def get_billname_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    BillID: Optional[int] = None,
    Name: Optional[str] = None,
    NameHistoryTypeID: Optional[int] = None,
    NameHistoryTypeDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_billname table"""
    query_params = request.query_params.items()
    order_by = '"BillNameID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_billname"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_billname/{BillNameID}',
            response_model=bills.KnsBillName,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_name(BillNameID: int):
    """Route for single "bills_kns_billname" table"""
    data = DB.get_single_data('bills_kns_billname', 'BillNameID', BillNameID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_documentbill/list",
            status_code=200,
            response_model=List[bills.KnsDocumentBill],
            responses={422: errors.LIMIT_ERROR})
async def get_documentbill_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    BillID: Optional[int] = None,
    GroupTypeID: Optional[int] = None,
    GroupTypeDesc: Optional[str] = None,
    ApplicationID: Optional[int] = None,
    ApplicationDesc: Optional[str] = None,
    FilePath: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_documentbill table"""
    query_params = request.query_params.items()
    order_by = '"DocumentBillID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_documentbill"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_documentbill/{DocumentBillID}',
            response_model=bills.KnsDocumentBill,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_document_bill(DocumentBillID: int):
    """Route for single "bills_kns_documentbill" table"""
    data = DB.get_single_data('bills_kns_documentbill', 'DocumentBillID', DocumentBillID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_bill__airflow/list",
            status_code=200,
            response_model=List[bills.KnsBillAirflow],
            responses={422: errors.LIMIT_ERROR})
async def get_bill_airflow_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    SubTypeID: Optional[int] = None,
    SubTypeDesc: Optional[str] = None,
    PrivateNumber: Optional[int] = None,
    CommitteeID: Optional[int] = None,
    StatusID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_bill__airflow table"""
    query_params = request.query_params.items()
    order_by = '"BillID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_bill__airflow"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_bill__airflow/{BillID}',
            response_model=bills.KnsBillAirflow,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_airflow(BillID: int):
    """Route for single "bills_kns_bill__airflow" table"""
    data = DB.get_single_data('bills_kns_bill__airflow', 'BillID', BillID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_billhistoryinitiator/list",
            status_code=200,
            response_model=List[bills.KnsBillHistoryInitiator],
            responses={422: errors.LIMIT_ERROR})
async def get_billhistoryinitiator_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    BillID: Optional[int] = None,
    PersonID: Optional[int] = None,
    IsInitiator: Optional[bool] = None,
    StartDate: Optional[datetime] = None,
    EndDate: Optional[datetime] = None,
    ReasonID: Optional[int] = None,
    ReasonDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_billhistoryinitiator table"""
    query_params = request.query_params.items()
    order_by = '"BillHistoryInitiatorID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_billhistoryinitiator"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_billhistoryinitiator/{BillHistoryInitiatorID}',
            response_model=bills.KnsBillHistoryInitiator,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill_history_initiator(BillHistoryInitiatorID: int):
    """Route for single "bills_kns_billhistoryinitiator" table"""
    data = DB.get_single_data('bills_kns_billhistoryinitiator', 'BillHistoryInitiatorID', BillHistoryInitiatorID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/bills_kns_bill/list",
            status_code=200,
            response_model=List[bills.KnsBill],
            responses={422: errors.LIMIT_ERROR})
async def get_bill_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    SubTypeID: Optional[int] = None,
    SubTypeDesc: Optional[str] = None,
    PrivateNumber: Optional[int] = None,
    CommitteeID: Optional[int] = None,
    StatusID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list bills_kns_bill table"""
    query_params = request.query_params.items()
    order_by = '"BillID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM bills_kns_bill"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/bills_kns_bill/{BillID}',
            response_model=bills.KnsBill,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_bill(BillID: int):
    """Route for single "bills_kns_bill" table"""
    data = DB.get_single_data('bills_kns_bill', 'BillID', BillID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

