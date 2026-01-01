from pydantic import BaseModel
from typing import Dict, List
from datetime import datetime
from pydantic import HttpUrl
from app.schemas.enums import FileType


class KnsDocumentCommitteeSessionDataservice(BaseModel):
    DocumentCommitteeSessionID: int = 71335
    CommitteeSessionID: int = 66045
    GroupTypeID: int = 23
    GroupTypeDesc: str = "פרוטוקול ועדה"
    ApplicationID: int = 1
    ApplicationDesc: str = "DOC"
    FilePath: HttpUrl = "https://fs.knesset.gov.il//16/Committees/16_ptv_71308.doc"
    LastUpdatedDate: datetime = "2010-06-02T20:32:33"


class KnsJointCommittee(BaseModel):
    JointCommitteeID: int = 1
    CommitteeID: int = 37
    ParticipantCommitteeID: int = 21
    LastUpdatedDate: datetime = "2015-03-20T12:02:57"


class KnsCommitteeAirflow(BaseModel):
    CommitteeID: int = 1
    Name: str = "ועדת הכנסת"
    CategoryID: int | None = 1
    CategoryDesc: str | None = "ועדת הכנסת"
    KnessetNum: int | None = 15
    CommitteeTypeID: int | None = 70
    CommitteeTypeDesc: str | None = "ועדת הכנסת"
    Email: str | None = "vadatk@knesset.gov.il"
    StartDate: datetime = "1999-06-07T00:00:00"
    FinishDate: datetime | None = "2001-06-07T00:00:00"
    AdditionalTypeID: int | None = 991
    AdditionalTypeDesc: str | None = "קבועה"
    ParentCommitteeID: int | None = 39
    CommitteeParentName: str | None = None
    IsCurrent: bool = "true"
    LastUpdatedDate: datetime = "2017-04-24T16:47:06"


class BuildMeetings(BaseModel):
    CommitteeSessionID: int = 64529
    Number: int | None = 460
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = "פתוחה"
    CommitteeID: int = 29
    Location: str | None = None
    SessionUrl: HttpUrl = "http://main.knesset.gov.il/Activity/committees/Pages/AllCommitteesAgenda.aspx?Tab=3&ItemID=64529"
    BroadcastUrl: HttpUrl | None = None
    StartDate: datetime = "2003-03-12T10:30:00"
    FinishDate: datetime | None = "2003-03-12T23:59:00"
    Note: str | None = None
    LastUpdatedDate: datetime = "2017-06-13T15:44:21"
    protocol_extension: str | None = ".doc"
    text_filename: str | None = None
    parts_filename: str | None = None
    topics: List[str] | None = []
    mks: List[str] = []
    invitees: List[Dict[str, str]] = []
    legal_advisors: List[str] = []
    manager: List[str] = []
    attended_mk_individual_ids: List[int] = []


class DocumentBackgroundMaterialTitles(BaseModel):
    DocumentCommitteeSessionID: int = 0
    CommitteeSessionID: int = 64776
    CommitteeID: int = 25
    FilePath: HttpUrl = "https://fs.knesset.gov.il/\\16\\Committees\\16_cs_bg_339777.pdf"
    title: str = "חומר רקע"


class JoinedMeetings(BaseModel):
    CommitteeSessionID: int = 64515
    Number: int | None = 2
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = "פתוחה"
    CommitteeID: int = 22
    Location: str | None = None
    SessionUrl: HttpUrl = "http://main.knesset.gov.il/Activity/committees/Pages/AllCommitteesAgenda.aspx?Tab=3&ItemID=64515"
    BroadcastUrl: HttpUrl | None = None
    StartDate: datetime = "2003-02-25T10:30:00"
    FinishDate: datetime | None = "2005-02-25T10:30:00"
    Note: str | None = None
    LastUpdatedDate: datetime = "2012-09-19T15:27:32"
    protocol_extension: str | None = ".doc"
    text_filename: str | None = None
    parts_filename: str | None = None
    topics: List[str] | None = []


class KnsCmtSitecode(BaseModel):
    CmtSiteCode: int = 1
    KnsID: int = 1
    SiteId: int = 1


class MeetingProtocolsParts(BaseModel):
    DocumentCommitteeSessionID: int = 71333
    CommitteeSessionID: int = 65782
    GroupTypeID: int = 23
    GroupTypeDesc: str = "פרוטוקול ועדה"
    ApplicationID: int = 1
    ApplicationDesc: FileType = "DOC"
    FilePath: HttpUrl = "http://fs.knesset.gov.il//16/Committees/16_ptv_71307.doc"
    LastUpdatedDate: datetime = "2010-06-02T20:32:33"
    KnessetNum: int = 16
    protocol_extension: str | None = ".doc"
    parsed_filename: str | None = None
    filesize: int | None = None
    crc32c: str | None = None
    error: str | None = None


class BuildRenderedMeetingsStats(BaseModel):
    CommitteeSessionID: int = 64529
    num_speech_parts: int = 7


class KnsDocumentCommitteeSession(BaseModel):
    DocumentCommitteeSessionID: int = 138775
    CommitteeSessionID: int = 311813
    GroupTypeID: int = 23
    GroupTypeDesc: str = "פרוטוקול ועדה"
    ApplicationID: int = 1
    ApplicationDesc: str = "DOC"
    FilePath: HttpUrl = "https://fs.knesset.gov.il//17/Committees/17_ptv_137257.doc"
    LastUpdatedDate: datetime = "2010-06-03T10:09:32"


class KnsCmtSessionItem(BaseModel):
    CmtSessionItemID: int = 28006
    ItemID: int = 74814
    CommitteeSessionID: int = 64516
    Ordinal: int | None = 20
    StatusID: int | None = 108
    Name: str | None = "שינויים בתקציב לשנת 2003"
    ItemTypeID: int | None = 11
    LastUpdatedDate: datetime = "2012-09-20T22:23:49"


class KnsCommitteeSession(BaseModel):
    CommitteeSessionID: int = 64515
    Number: int = 460
    KnessetNum: int = 16
    TypeID: int = 161
    TypeDesc: str = "פתוחה"
    CommitteeID: int = 22
    Location: str = None
    SessionUrl: HttpUrl = "http://main.knesset.gov.il/Activity/committees/Pages/AllCommitteesAgenda.aspx?Tab=3&ItemID=64515"
    BroadcastUrl: HttpUrl = None
    StartDate: datetime = "2003-02-25T10:30:00"
    FinishDate: datetime = "2005-02-25T10:30:00"
    Note: str = None
    LastUpdatedDate: datetime = "2012-09-19T15:27:32"


class KnsCommittee(BaseModel):
    CommitteeID: int = 1
    Name: str = "ועדת הכנסת"
    CategoryID: int | None = 1
    CategoryDesc: str | None = "ועדת הכנסת"
    KnessetNum: int | None = 15
    CommitteeTypeID: int | None = 70
    CommitteeTypeDesc: str | None = "ועדת הכנסת"
    Email: str | None = "vadatk@knesset.gov.il"
    StartDate: datetime | None = "1999-06-07T00:00:00"
    FinishDate: datetime = "2001-06-07T00:00:00"
    AdditionalTypeID: int | None = 991
    AdditionalTypeDesc: str | None = "קבועה"
    ParentCommitteeID: int | None = 39
    CommitteeParentName: str | None = None
    IsCurrent: bool = "true"
    LastUpdatedDate: datetime = "2017-04-24T16:47:06"

