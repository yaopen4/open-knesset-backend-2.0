from pydantic import BaseModel
from typing import List, Union


class MinisterByIndividual(BaseModel):
    mk_individual_id: int = 69
    FirstName: str = "ישראל"
    LastName: str = "כץ"
    GenderDesc: str = "זכר"
    Email: str = "yiskatz@knesset.gov.il"
    altnames: List[str] = ["ישראל כץ"]
    mk_individual_photo: str = "https://oknesset.org/static/img/Male_portrait_placeholder_cropped.jpg"
    faction_name: str = "הליכוד"
    ministers: str = "[משרד האנרגיה והתשתיות: שר]"
    IsChairPerson: bool = True
    knessets: str = "14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25"
    committees: List[Union[None, str]] = [None]
    year_total_hours_attended: str = ""


class MinisterByPersonal(BaseModel):
    PersonID: int = 468
    FirstName: str = "ישראל"
    LastName: str = "כץ"
    GenderDesc: str = "זכר"
    Email: str = "yiskatz@knesset.gov.il"
    altnames: List[str] = ["ישראל כץ"]
    mk_individual_photo: str = "https://oknesset.org/static/img/Male_portrait_placeholder_cropped.jpg"
    faction_name: str = "הליכוד"
    ministers: str = "[משרד האנרגיה והתשתיות: שר]"
    IsChairPerson: bool = True
    knessets: str = "14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25"
    committees: List[Union[None, str]] = [None]
    year_total_hours_attended: str = ""

