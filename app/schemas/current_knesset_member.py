from pydantic import BaseModel
from typing import List, Union


class KnessetMemberByIndividual(BaseModel):
    mk_individual_id: int = 214
    FirstName: str = "אביגדור"
    LastName: str = "ליברמן"
    GenderDesc: str = "זכר"
    Email: str | None = "aliberman@knesset.gov.il"
    altnames: List[str] = ["אביגדור ליברמן"]
    mk_individual_photo: str | None = "https://oknesset.org/static/img/Male_portrait_placeholder_cropped.jpg"
    faction_name: str = "ישראל ביתנו בראשות אביגדור ליברמן"
    IsChairPerson: bool = True
    knessets: str = "15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25"
    committees: List[Union[None, str]] = []
    year_total_hours_attended: str = ""


class KnessetMemberByPersonal(BaseModel):
    PersonID: int = 427
    FirstName: str = "אביגדור"
    LastName: str = "ליברמן"
    GenderDesc: str = "זכר"
    Email: str | None = "aliberman@knesset.gov.il"
    altnames: List[str] = ["אביגדור ליברמן"]
    mk_individual_photo: str | None = "https://oknesset.org/static/img/Male_portrait_placeholder_cropped.jpg"
    faction_name: str = "ישראל ביתנו בראשות אביגדור ליברמן"
    IsChairPerson: bool = True
    knessets: str = "15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25"
    committees: List[Union[None, str]] = []
    year_total_hours_attended: str = ""

