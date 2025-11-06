import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0)

def save_message(session_id: str, role: str, message: str):
    key = f"chat:{session_id}"
    history = get_history(session_id)
    history.append({"role": role, "message": message})
    r.set(key, json.dumps(history))

def get_history(session_id: str):
    key = f"chat:{session_id}"
    data = r.get(key)
    return json.loads(data) if data else []
