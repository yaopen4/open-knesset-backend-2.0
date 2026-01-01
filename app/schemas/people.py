from pydantic import BaseModel
from typing import Dict, List, Literal, Union
from datetime import datetime
from pydantic import HttpUrl


class PlenumSessionVotersStats(BaseModel):
    knesset: int = 16
    plenum: int = 1
    assembly: int = 1
    pagra: int = 0
    faction_id: int = 53
    mk_id: int = 1
    voted_sessions: int = 0
    total_sessions: int = 10
    voted_sessions_percent: int = 0


class CommitteesJoinedMeetings(BaseModel):
    CommitteeSessionID: int = 64516
    Number: int | None = 2
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = "פתוחה"
    CommitteeID: int = 21
    Location: str | None = None
    SessionUrl: HttpUrl = "http://main.knesset.gov.il/Activity/committees/Pages/AllCommitteesAgenda.aspx?Tab=3&ItemID=64516"
    BroadcastUrl: HttpUrl | None = None
    StartDate: datetime = "2003-02-24T10:00:00"
    FinishDate: datetime | None = "2005-02-24T10:00:00"
    Note: str | None = None
    LastUpdatedDate: datetime = "2012-09-19T15:27:32"
    text_file_name: str | None = None
    text_file_size: int | None = None
    topics: List[str] | None = []


class CommitteesMeetingAttendees(BaseModel):
    CommitteeSessionID: int = 64516
    Number: int | None = 2
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = "פתוחה"
    CommitteeID: int = 21
    Location: str | None = None
    SessionUrl: HttpUrl = "http://main.knesset.gov.il/Activity/committees/Pages/AllCommitteesAgenda.aspx?Tab=3&ItemID=64516"
    BroadcastUrl: HttpUrl | None = None
    StartDate: datetime = "2003-02-24T10:00:00"
    FinishDate: datetime | None = "2005-02-24T10:00:00"
    Note: str | None = None
    LastUpdatedDate: datetime = "2019-05-16T11:33:28"
    download_crc32c: str | None = None
    download_filename: str | None = None
    download_filesize: int | None = None
    parts_crc32c: str | None = None
    parts_filesize: int | None = None
    parts_parsed_filename: str | None = None
    text_crc32c: str | None = None
    text_filesize: int | None = None
    text_parsed_filename: str | None = None
    item_ids: List[int] | None = []
    item_type_ids: List[int] | None = []
    topics: List[str] | None = []
    committee_name: str | None = None
    bill_names: List[str] = []
    bill_types: List[str] = []
    related_to_legislation: bool | None = None
    mks: List[str] | None = []
    invitees: List[Dict[str, str]] | None = []
    legal_advisors: List[str] | None = []
    manager: List[str] | None = []
    financial_advisors: List[str] | None = []
    attended_mk_individual_ids: List[int] = []


class PartyDisciplineStats(BaseModel):
    knesset: int = 16
    plenum: int = 2
    assembly: int = 1
    pagra: int = 0
    faction_id: int = 24
    mk_id: int = 1
    undisciplined_votes: int = 0
    disciplined_votes: int = 112
    total_votes: int = 961
    undisciplined_votes_percent: int = 0
    disciplined_votes_percent: int = 11


class CommitteesMeetingAttendeesMksFullStats(BaseModel):
    knesset: int = 16
    plenum: int = 1
    assembly: int = 1
    pagra: int = 0
    committee_id: int = 21
    faction_id: int = 53
    mk_id: int = 1
    attended_meetings: int = 0
    protocol_meetings: int = 1
    open_meetings: int = 1
    attended_meetings_percent: int = 0
    attended_meetings_relative_percent: int = 0


class CommitteesMeetingSpeakerStats(BaseModel):
    CommitteeSessionID: int = 100017
    parts_crc32c: str = "EIzyDg=="
    part_index: int = 0
    header: str = "סדר היום"
    body_length: int = 214
    body_num_words: int = 25
    part_categories: str = "משפטן"
    name_role: str = None
    mk_individual_id: int = 1
    mk_individual_faction: str = None


class PlenumSessionVoters(BaseModel):
    PlenumSessionID: int = 9626
    Number: int | None = 1
    KnessetNum: int = 16
    Name: str = "ישיבת מליאה בתאריך 17/02/2003 בשעה: 16:00"
    StartDate: datetime = "2003-02-17T16:00:00"
    FinishDate: datetime | None = "2004-02-17T16:00:00"
    IsSpecialMeeting: bool = "false"
    LastUpdatedDate: datetime = "2013-10-03T16:21:47"
    voter_mk_ids: List[int] | None = []


class MkVotedAgainstMajority(BaseModel):
    vote_id: int = 10
    mk_id: int = 114
    faction_id: int = 24
    vote_knesset: int = 16
    vote_plenum: int = 2
    vote_assembly: int = 1
    vote_pagra: bool = 'false'
    vote_datetime: datetime = '2003-10-20T20:09:00'
    vote_majority: str = 'against'
    voted_against_majority: bool = 'false'


class MkPartyDisciplineKnesset20(BaseModel):
    vote_id: int = 31582
    vote_url: HttpUrl = 'http://www.knesset.gov.il/vote/heb/Vote_Res_Map.asp?vote_id_t=31582'
    vote_datetime: datetime = '2018-12-31T15:27:00'
    vote_knesset: int = 20
    vote_plenum: int = 5
    vote_assembly: int = 1
    vote_pagra: bool = 'false'
    mk_id: int = 868
    mk_name: str = 'יעל גרמן'
    faction_id: int = 904
    faction_name: str = 'יש עתיד'
    vote_majority: str = 'pro'


class CommitteesMeetingAttendeesMksStats(BaseModel):
    knesset_num: int = 16
    committee_id: int = 21
    committee_name: str = 'ועדת הכספים'
    meeting_start_date: datetime = '2003-02-24T10:00:00'
    meeting_topics: str = None
    mk_id: int = 64
    mk_name: str = 'איתן כבל'
    mk_membership_committee_names: str = None
    mk_faction_id: int = 24
    mk_faction_name: str = 'הליכוד'


class MembersJoinedMks(BaseModel):
    mk_individual_id: int = 1
    mk_status_id: int = 1
    mk_individual_name: str = 'אדלשטיין'
    mk_individual_name_eng: str | None = 'Edelstein'
    mk_individual_first_name: str = 'יולי יואל'
    mk_individual_first_name_eng: str | None = 'Yuli-Yoel'
    mk_individual_email: str | None = None
    mk_individual_photo: HttpUrl | None = None
    PersonID: int = 532
    LastName: str = 'אדלשטיין'
    FirstName: str = 'יולי יואל'
    GenderID: int = 251
    GenderDesc: Literal['זכר', 'נקבה'] = 'זכר'
    Email: str | None = None
    IsCurrent: bool = 'true'
    LastUpdatedDate: datetime = '2015-11-15T19:51:25'
    positions: List[Dict[str, Union[str, int, datetime]]] = []
    altnames: List[str] = []


class CommitteesMeetingAttendeesMks(BaseModel):
    CommitteeSessionID: int = 64529
    Number: int | None = 67
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = 'פתוחה'
    CommitteeID: int | None = 29
    Location: str | None = None
    SessionUrl: HttpUrl | None = None
    BroadcastUrl: str | None = None
    StartDate: datetime = '2003-03-12T10:30:00'
    FinishDate: datetime | None = '2003-03-12T23:59:00'
    Note: str | None = None
    LastUpdatedDate: datetime = '2017-06-13T15:44:21'
    protocol_extension: str | None = None
    text_filename: str | None = None
    parts_filename: str | None = None
    topics: List[str] | None = []
    mks: List[str] = []
    invitees: List[Dict[str, str]] = []
    legal_advisors: List[str] = []
    manager: List[str] = []

