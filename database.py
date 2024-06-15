from pymongo import MongoClient
import datetime

def get_database():
    client = MongoClient('mongodb://localhost:27017/')
    return client['SneakersHeaven']

def log_audit(db, action, entity, details):
    audit_data = {
        "action": action,
        "entity": entity,
        "details": details,
        "timestamp": datetime.datetime.now()
    }
    db.auditorias.insert_one(audit_data)

