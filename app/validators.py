import uuid


def parse_uuid(uuid_string):

    try:
        # Check if data is in valid UUID format
        return str(uuid.UUID(uuid_string))
    except ValueError:
        return False
