import redisConnector
import json


r = redisConnector.get_redis_connection()
r.set(1, json.dumps({"function": 1, "passage": 12, "sentence": 13}), ex=5)
value = json.loads(r.get(1))
print(value["function"])
