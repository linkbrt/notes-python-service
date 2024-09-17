import os
import jwt
import json
from json import JSONEncoder
from jwt.utils import base64url_encode


jwt_key = os.environ.get("JWT_SECRET")

encoded = jwt.encode({"username": "admin", "admin": True}, jwt_key, algorithm="HS256")

print(encoded)

from jwt.api_jws import encode


json_header = json.dumps(
            {"typ": "JWT", "alg": "none"}, separators=(",", ":"), cls=JSONEncoder
        ).encode()

print(base64url_encode(json_header))


eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOnRydWV9.nL305gc31BSlzQ9tCn89sP1pTCMrBqnTuxdNHi2DS3E

decoded = jwt.decode(encoded, jwt_key, algorithms="HS256")

# print(decoded)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOnRydWV9.nL305gc31BSlzQ9tCn89sP1pTCMrBqnTuxdNHi2DS3E

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiYWRtaW4iOmZhbHNlfQ.yRhbtEnBab1UfHM95yP6Ukz3EQrQqP6lwZFcqwvKwjg