import json
from connection.redisConnector import get_redis_connection
ExpireTime = 100


def get_user_data(user_id: int):
    try:
        r = get_redis_connection()
        value = r.get(str(user_id))
        if value:
            return json.loads(value)
        return None
    except:
        return None


def set_user_data(user_id: int, data: dict):
    try:
        r = get_redis_connection()
        r.set(str(user_id), json.dumps(data), ex=ExpireTime)
        return True
    except:
        return False


def remove_user_data(user_id: int):
    try:
        r = get_redis_connection()
        r.delete(str(user_id))
        return True
    except:
        return False