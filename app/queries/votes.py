# Votes-related SQL queries

def get_vote_rslts_hdr_approved_list():
    return "SELECT * FROM votes_view_vote_rslts_hdr_approved"

def get_vote_rslts_kmmbr_shadow_extra_list():
    return "SELECT * FROM votes_vote_rslts_kmmbr_shadow_extra"

def get_vote_mk_individual_list():
    return "SELECT * FROM votes_view_vote_mk_individual"

def get_vote_rslts_kmmbr_shadow_list():
    return "SELECT * FROM votes_vote_rslts_kmmbr_shadow"

def get_vote_rslts_hdr_approved_extra_list():
    return "SELECT * FROM votes_view_vote_rslts_hdr_approved_extra"

def get_vote_result_type_list():
    return "SELECT * FROM votes_vote_result_type"

