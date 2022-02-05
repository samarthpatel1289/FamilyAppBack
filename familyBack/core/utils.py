from datetime import datetime
from core import constants as coreConstants

def strToDateTime(date):
    datetime_object = datetime.strptime(date, coreConstants.DATE_FORMAT)
    return datetime_object

def validate_phone(data):
    if len(str(data)) > 10:
        return False
    return True
