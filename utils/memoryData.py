import json
from connection.redisConnector import get_redis_connection
ExpireTime = 600


def get_user_data(user_id):
    try:
        r = get_redis_connection()
        value = r.get(user_id)
        if value:
            return json.loads(value)
        return None
    except:
        return None


def set_user_data(user_id, data):
    try:
        r = get_redis_connection()
        r.set(user_id, json.dumps(data), ex=ExpireTime)
        return True
    except:
        return False
