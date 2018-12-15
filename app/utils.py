import datetime


def get_date_utcnow():
    """
    Generate date utcnow
    :return:
    """
    return datetime.datetime.utcnow()


def get_str_from_date_isoformat():
    """
    Generate date now in isoformat from utc
    :return:
    """
    return get_date_utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
