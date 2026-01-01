# People-related SQL queries

def get_plenum_session_voters_stats_list():
    return "SELECT * FROM people_plenum_session_voters_stats"

def get_committees_joined_meetings_list():
    return "SELECT * FROM people_committees_joined_meetings"

def get_committees_meeting_attendees_list():
    return "SELECT * FROM people_committees_meeting_attendees"

def get_mk_party_discipline_stats_list():
    return "SELECT * FROM people_mk_party_discipline_stats"

def get_committees_meeting_attendees_mks_full_stats_list():
    return "SELECT * FROM people_committees_meeting_attendees_mks_full_stats"

def get_committees_meeting_speaker_stats_list():
    return "SELECT * FROM people_committees_meeting_speaker_stats"

def get_plenum_session_voters_list():
    return "SELECT * FROM people_plenum_session_voters"

def get_mk_voted_against_majority_list():
    return "SELECT * FROM people_mk_voted_against_majority"

def get_mk_party_discipline_knesset_20_list():
    return "SELECT * FROM people_mk_party_discipline_knesset_20"

def get_committees_meeting_attendees_mks_stats_list():
    return "SELECT * FROM people_committees_meeting_attendees_mks_stats"

def get_committees_meeting_attendees_mks_stats_errors_list():
    return "SELECT * FROM people_committees_meeting_attendees_mks_stats_errors"

def get_members_joined_mks_list():
    return "SELECT * FROM people_members_joined_mks"

def get_committees_meeting_attendees_mks_list():
    return "SELECT * FROM people_committees_meeting_attendees_mks"

