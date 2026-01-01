from fastapi import APIRouter, HTTPException, status, Request
from typing import List, Optional
from datetime import datetime

from app.schemas import laws
from app.schemas import errors

import api.db as DB

router = APIRouter(tags=['laws'])


@router.get("/laws_kns_document_law/list",
            status_code=200,
            response_model=List[laws.DocumentLaw],
            responses={422: errors.LIMIT_ERROR})
async def get_document_law_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    LawID: Optional[int] = None,
    GroupTypeID: Optional[int] = None,
    GroupTypeDesc: Optional[str] = None,
    ApplicationID: Optional[int] = None,
    ApplicationDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_document_law table"""
    query_params = request.query_params.items()
    order_by = '"DocumentLawID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_document_law"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_document_law/{DocumentLawID}',
            response_model=laws.DocumentLaw,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_document_law(DocumentLawID: int):
    """Route for single laws_kns_document_law table"""
    data = DB.get_single_data('laws_kns_document_law', 'DocumentLawID', DocumentLawID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_israel_law/list",
            status_code=200,
            response_model=List[laws.IsraelLaw],
            responses={422: errors.LIMIT_ERROR})
async def get_israel_law_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    IsBasicLaw: Optional[bool] = None,
    IsFavoriteLaw: Optional[bool] = None,
    IsBudgetLaw: Optional[bool] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_israel_law table"""
    query_params = request.query_params.items()
    order_by = '"IsraelLawID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_israel_law"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_israel_law/{IsraelLawID}',
            response_model=laws.IsraelLaw,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_israel_law(IsraelLawID: int):
    """Route for single laws_kns_israel_law table"""
    data = DB.get_single_data('laws_kns_israel_law', 'IsraelLawID', IsraelLawID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_israel_law_binding/list",
            status_code=200,
            response_model=List[laws.IsraelLawBinding],
            responses={422: errors.LIMIT_ERROR})
async def get_israel_law_binding_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    IsraelLawID: Optional[int] = None,
    IsraelLawReplacedID: Optional[int] = None,
    LawID: Optional[int] = None,
    LawTypeID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_israel_law_binding table"""
    query_params = request.query_params.items()
    order_by = '"IsraelLawBinding" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_israel_law_binding"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_israel_law_ministry/list",
            status_code=200,
            response_model=List[laws.IsraelLawMinistry],
            responses={422: errors.LIMIT_ERROR})
async def get_israel_law_ministry_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    IsraelLawID: Optional[int] = None,
    GovMinistryID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_israel_law_ministry table"""
    query_params = request.query_params.items()
    order_by = '"LawMinistryID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_israel_law_ministry"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_israel_law_ministry/{LawMinistryID}',
            response_model=laws.IsraelLawMinistry,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_israel_law_ministry(LawMinistryID: int):
    """Route for single laws_kns_israel_law_ministry table"""
    data = DB.get_single_data('laws_kns_israel_law_ministry', 'LawMinistryID', LawMinistryID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_law/list",
            status_code=200,
            response_model=List[laws.KnsLaw],
            responses={422: errors.LIMIT_ERROR})
async def get_law_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    TypeID: Optional[int] = None,
    TypeDesc: Optional[str] = None,
    SubTypeID: Optional[int] = None,
    SubTypeDesc: Optional[str] = None,
    KnessetNum: Optional[int] = None,
    Name: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_law table"""
    query_params = request.query_params.items()
    order_by = '"LawID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_law"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_law/{LawID}',
            response_model=laws.KnsLaw,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_law(LawID: int):
    """Route for single laws_kns_law table"""
    data = DB.get_single_data('laws_kns_law', 'LawID', LawID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_israel_law_name/list",
            status_code=200,
            response_model=List[laws.IsraelLawName],
            responses={422: errors.LIMIT_ERROR})
async def get_israel_law_name_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    IsraelLawID: Optional[int] = None,
    LawID: Optional[int] = None,
    LawTypeID: Optional[int] = None,
    Name: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_israel_law_name table"""
    query_params = request.query_params.items()
    order_by = '"IsraelLawNameID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_israel_law_name"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_israel_law_name/{IsraelLawNameID}',
            response_model=laws.IsraelLawName,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_israel_law_name(IsraelLawNameID: int):
    """Route for single laws_kns_israel_law_name table"""
    data = DB.get_single_data('laws_kns_israel_law_name', 'IsraelLawNameID', IsraelLawNameID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_law_binding/list",
            status_code=200,
            response_model=List[laws.LawBinding],
            responses={422: errors.LIMIT_ERROR})
async def get_law_binding_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    LawID: Optional[int] = None,
    LawTypeID: Optional[int] = None,
    IsraelLawID: Optional[int] = None,
    ParentLawID: Optional[int] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_law_binding table"""
    query_params = request.query_params.items()
    order_by = '"LawBindingID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_law_binding"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_law_binding/{LawBindingID}',
            response_model=laws.LawBinding,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_law_binding(LawBindingID: int):
    """Route for single laws_kns_law_binding table"""
    data = DB.get_single_data('laws_kns_law_binding', 'LawBindingID', LawBindingID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get("/laws_kns_israel_law_classification/list",
            status_code=200,
            response_model=List[laws.IsraelLawClassification],
            responses={422: errors.LIMIT_ERROR})
async def get_israel_law_classification_list(
    request: Request,
    limit: int = 100,
    offset: int = 0,
    IsraelLawID: Optional[int] = None,
    ClassificiationID: Optional[int] = None,
    ClassificiationDesc: Optional[str] = None,
    LastUpdatedDate: Optional[datetime] = None
):
    """Route for list laws_kns_israel_law_classification table"""
    query_params = request.query_params.items()
    order_by = '"LawClassificiationID" desc'
    qs_parts = []
    for key, value in query_params:
        if key not in ['limit', 'offset', 'order_by']:
            qs_parts.append(f"{key}={value}")
    qs = '&'.join(qs_parts)
    query = "SELECT * FROM laws_kns_israel_law_classification"
    data = DB.get_data_list(query, limit, offset, order_by, qs)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data


@router.get('/laws_kns_israel_law_classification/{LawClassificiationID}',
            response_model=laws.IsraelLawClassification,
            responses={404: errors.NO_DATA_FOUND_ERROR})
async def get_israel_law_classification(LawClassificiationID: int):
    """Route for single laws_kns_israel_law_classification table"""
    data = DB.get_single_data('laws_kns_israel_law_classification', 'LawClassificiationID', LawClassificiationID)
    if isinstance(data, TypeError):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'error': type(data).__name__, 'msg': str(data)})
    return data

