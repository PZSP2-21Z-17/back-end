from fastapi import status, HTTPException


def HTTPUnauthorized() -> HTTPException:
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def HTTPBadRequest() -> HTTPException:
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


def HTTPForbidden() -> HTTPException:
    return HTTPException(status_code=status.HTTP_403_FORBIDDEN)
