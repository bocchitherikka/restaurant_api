from fastapi import HTTPException


class APIException(HTTPException):
    def __init__(self, status_code: int, detail: str = "Error"):
        super().__init__(
            status_code=status_code,
            detail=detail
        )


class ObjectNotFoundException(APIException):
    def __init__(self, klass):
        super().__init__(
            status_code=404,
            detail=f"{klass.__name__} not found!"
        )


class TableOccupiedException(APIException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="This table is occupied at the time!"
        )


class TableHasReservationsException(APIException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="This table has reservations!"
        )
