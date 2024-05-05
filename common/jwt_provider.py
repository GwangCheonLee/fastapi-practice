from datetime import datetime, timedelta, timezone

from jose import jwt


def create_access_token(data: dict, expires_delta: timedelta, secret_key: str, algorithm: str) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt
