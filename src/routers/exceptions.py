from http.client import HTTPException

from fastapi import status

def HTTPUnauthorized() -> HTTPException:
    HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
