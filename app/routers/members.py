from fastapi import APIRouter, HTTPException, status, Request, Query
from typing import List, Optional, Union

from app.schemas import user_friendly, members
from app.schemas import current_knesset_member, current_minister
from app.schemas import errors
from app.queries import members as member_queries
from app.core import query_builder as DB

# Import old api module for backwards compatibility during migration
import api.db as OLD_DB
from api import queries as QUERY

router = APIRouter(tags=['user friendly'])


@router.get("/members", status_code=200,
            description="""
            By default, this endpoint returns information about current Knesset members,
            along with their details for the current Knesset.

            You can customize the results using the following parameters:
            - `knesset_term` (int, optional): Specify a Knesset number to filter members for a specific term.
            - `is_current` (bool, optional): Set to True to retrieve details about current Knesset members,
               or False to include details for all Knesset members that are not currently Knesset members.

            Note: If 'factions' for some Knesset member in the output contains null,
                  it indicates that the Knesset member did not serve during the specified term.
            """,
            summary="""Retrieve details of Knesset members for a specified period.""",
            response_model=List[user_friendly.Member])
async def get_friendly_members_list(
    knesset_term: Optional[int] = None,
    is_current: Optional[bool] = True,
):
    query = QUERY.get_members()
    data = OLD_DB.get_members(query, is_current, knesset_term)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/{mk_individual_id}", status_code=200,
            description="""
            By default, this endpoint returns information about current Knesset term.

            You can customize the results using the following parameters:
            - `mk_individual_id` (int): Specify the ID of a Knesset member.
            - `knesset_term` (int, optional): Specify a Knesset term.

            Note: If 'factions' in the output contains null, it indicates that the Knesset member did not serve during the specified term.
            """,
            summary="""Retrieve details of some Knesset member for a specified term.""",
            response_model=user_friendly.Member)
async def get_friendly_member(
    mk_individual_id: int = None,
    knesset_term: Optional[int] = None,
):
    query = QUERY.get_member()
    data = OLD_DB.get_member(query, mk_individual_id, knesset_term)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/search/by-committee/{committee}", status_code=200,
            description="""
            You can customize the results using the following parameters:

            - `committee` (int | str): Specify a committee ID or name.
            """,
            summary="""Return mk_individual_id of matching members filtered by committee ID or name.""",
            response_model=List[user_friendly.MkIndividualIDs])
async def get_friendly_member_by_committee(
    committee: Union[int, str]
):
    data = OLD_DB.get_member_by_committee(committee)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/search/by-faction/{faction}", status_code=200,
            description="""
            You can customize the results using the following parameters:

            - `faction` (int | str): Specify a faction ID or name.
            """,
            summary="""Return mk_individual_id of matching members factions.""",
            response_model=List[user_friendly.MkIndividualIDs])
async def get_friendly_member_by_faction(
    faction: Union[int, str]
):
    data = OLD_DB.get_member_by_faction(faction)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/search/by-faction_chairperson/{faction}",
            status_code=200,
            description="""
            You can customize the results using the following parameters:

            - `faction` (int | str): Specify a faction ID or name.
            """,
            summary="""Return the mk_individual_id of members who serve as the chairperson of a faction.""",
            response_model=List[user_friendly.MkIndividualIDs])
async def get_friendly_member_by_faction_chairperson(
    faction: Union[int, str]
):
    data = OLD_DB.get_member_by_faction_chairperson(faction)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/search/by-govministries/{govministry}",
            status_code=200,
            description="""
            You can customize the results using the following parameters:

            - `govministry` (int | str): Specify a govministry ID or name.
            """,
            summary="""Return the mk_individual_id of members who are affiliated with a government ministry.""",
            response_model=List[user_friendly.MkIndividualIDs])
async def get_friendly_member_by_govministries(
    govministry: Union[int, str]
):
    data = OLD_DB.get_member_by_govministries(govministry)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/search/by-name/{name}",
            status_code=200,
            description="""
            You can customize the results using the following parameters:

            - `name` (str): Specify a name or part of name of a member.
            """,
            summary="""Return the mk_individual_id of members who are affiliated with this name.""",
            response_model=List[user_friendly.MkIndividualIDs])
async def get_friendly_member_by_name(
    name: str
):
    data = OLD_DB.get_member_by_name(name)
    if isinstance(data, Exception):
        response_status = (status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/{mk_individual_id}/presence",
            status_code=200,
            description="""
            Retrieve information about the presence of a specific Knesset member.

            You can customize the results using the following parameters:
                - `mk_individual_id` (int): The unique identifier of the Knesset member.
            """,
            summary="""Get info about presence of some Knesset member""",
            response_model=List[user_friendly.MemberPresence],
            responses={
                404: errors.NO_DATA_FOUND_ERROR
            })
async def get_friendly_members_presence_list(
    limit: int = 100,
    offset: int = 0,
    mk_individual_id: int = None
):
    query = QUERY.get_members_presence(mk_individual_id)
    data = OLD_DB.get_data_list(query, limit, offset, None, None)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/{mk_individual_id}/attended_committee_meetings",
            status_code=200,
            description="""
            Retrieve information about the committee meetings attended by a specific Knesset member.

            You can customize the results using the following parameters:
                - `mk_individual_id` (int): The unique identifier of the Knesset member.
            """,
            summary="""Get info about the attended committee meetings of a Knesset member""",
            response_model=List[user_friendly.MemberAttendedCommitteeMeetings],
            responses={
                404: errors.NO_DATA_FOUND_ERROR
            })
async def get_friendly_members_attended_committee_meetings_list(
    limit: int = 100,
    offset: int = 0,
    mk_individual_id: int = None
):
    order_by = '"StartDate" desc nulls last,"CommitteeSessionID" desc'
    query = QUERY.get_members_attended_committee_meetings(mk_individual_id)
    data = OLD_DB.get_data_list(query, limit, offset, order_by, None)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/{mk_individual_id}/votes",
            status_code=200,
            description="""
            Retrieve information about the votes cast by a specific Knesset member.

            You can customize the results using the following parameters:
                - `mk_individual_id` (int): The unique identifier of the Knesset member.
            """,
            summary="""Get info about the the votes of a Knesset member""",
            response_model=List[user_friendly.MemberVote],
            responses={
                404: errors.NO_DATA_FOUND_ERROR
            })
async def get_friendly_members_votes_list(
    limit: int = 100,
    offset: int = 0,
    mk_individual_id: int = None
):
    order_by = 'vote_date desc, vote_time desc, session_id desc, sess_item_id desc'
    query = QUERY.get_members_votes(mk_individual_id)
    data = OLD_DB.get_data_list(query, limit, offset, order_by, None)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data


@router.get("/members/{mk_individual_id}/bills",
            status_code=200,
            description="""
            Retrieve information about the bills associated with a specific Knesset member.

            You can customize the results using the following parameters:
                - `mk_individual_id` (int): The unique identifier of the Knesset member.
            """,
            summary="""Get info about the the bills of a Knesset member""",
            response_model=List[user_friendly.MemberBill],
            responses={
                404: errors.NO_DATA_FOUND_ERROR
            })
async def get_friendly_members_bills_list(
    limit: int = 100,
    offset: int = 0,
    mk_individual_id: int = None
):
    order_by = '"BillID" desc'
    query = QUERY.get_members_bills(mk_individual_id)
    data = OLD_DB.get_data_list(query, limit, offset, order_by, None)
    if isinstance(data, Exception):
        response_status = (status.HTTP_404_NOT_FOUND
                           if isinstance(data, TypeError)
                           else status.HTTP_422_UNPROCESSABLE_ENTITY)
        raise HTTPException(
            status_code=response_status,
            detail={
                'error': type(data).__name__,
                'msg': str(data)})
    return data

