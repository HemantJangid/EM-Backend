from firebase_admin import auth
from emotorad import firebase_client
from emotorad.settings import SERVER


def get_firebase_user_id(token):
    if SERVER == 'development':
        return "1"

    try:
        result = auth.verify_id_token(token, firebase_client)
    except Exception as e:
        return None
    return result["user_id"]


def get_firebase_user_data(token):
    try:
        result = auth.verify_id_token(token, firebase_client)
    except Exception as e:
        return None
    return result
