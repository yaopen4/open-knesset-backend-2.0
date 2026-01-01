# Bills-related SQL queries

def get_billunion_list():
    return "SELECT * FROM bills_kns_billunion"

def get_billsplit_list():
    return "SELECT * FROM bills_kns_billsplit"

def get_billinitiator_list():
    return "SELECT * FROM bills_kns_billinitiator"

def get_billname_list():
    return "SELECT * FROM bills_kns_billname"

def get_documentbill_list():
    return "SELECT * FROM bills_kns_documentbill"

def get_bill_airflow_list():
    return "SELECT * FROM bills_kns_bill__airflow"

def get_billhistoryinitiator_list():
    return "SELECT * FROM bills_kns_billhistoryinitiator"

def get_bill_list():
    return "SELECT * FROM bills_kns_bill"

