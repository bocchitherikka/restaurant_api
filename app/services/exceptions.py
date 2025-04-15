from fastapi import HTTPException


class ObjectNotFoundException(HTTPException):
    def __init__(self, klass):
        super().__init__(
            status_code=404,
            detail=f"{klass.__name__} not found!"
        )


class TableOccupiedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="This table is occupied at the time!"
        )


class TableHasReservationsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail="This table has reservations!"
        )
