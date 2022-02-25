import connection.redisConnector
import json
from utils.functionList import Function
from data.memoryData import get_user_data, set_user_data


r = connection.redisConnector.get_redis_connection()
r.set(1, json.dumps({"function": Function.passageSentenceRecite.value, "passage": 12, "sentence": 13}), ex=5)
value = json.loads(r.get(1))
print(value["function"])

print(get_user_data(4))
print(set_user_data(4, {"function": Function.passageSentenceRecite.value, "passage": 12, "sentence": 13}))
print(get_user_data(4))
