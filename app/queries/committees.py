# Committees-related SQL queries

def get_documentcommitteesession_dataservice_list():
    return "SELECT * FROM committees_kns_documentcommitteesession_dataservice"

def get_jointcommittee_list():
    return "SELECT * FROM committees_kns_jointcommittee"

def get_committee_airflow_list():
    return "SELECT * FROM committees_kns_committee__airflow"

def get_build_meetings_list():
    return "SELECT * FROM committees_build_build_meetings"

def get_document_background_material_titles_list():
    return "SELECT * FROM committees_document_background_material_titles"

def get_joined_meetings_list():
    return "SELECT * FROM committees_joined_meetings"

def get_cmtsitecode_list():
    return "SELECT * FROM committees_kns_cmtsitecode"

def get_meeting_protocols_parts_list():
    return "SELECT * FROM committees_meeting_protocols_parts"

def get_build_rendered_meetings_stats_list():
    return "SELECT * FROM committees_build_rendered_meetings_stats"

def get_documentcommitteesession_list():
    return "SELECT * FROM committees_kns_documentcommitteesession"

def get_cmtsessionitem_list():
    return "SELECT * FROM committees_kns_cmtsessionitem"

def get_committeesession_list():
    return "SELECT * FROM committees_kns_committeesession"

def get_document_committee_sessions_for_parsing_list():
    return "SELECT * FROM committees_document_committee_sessions_for_parsing"

def get_download_document_committee_session_list():
    return "SELECT * FROM committees_download_document_committee_session"

def get_meeting_protocols_text_list():
    return "SELECT * FROM committees_meeting_protocols_text"

def get_committee_list():
    return "SELECT * FROM committees_kns_committee"

