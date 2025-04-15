from datetime import datetime
from pydantic import BaseModel, validator


class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

    @validator("reservation_time", pre=True)
    def parse_custom_time(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%d.%m.%Y %H:%M")
            except ValueError:
                raise ValueError("Wrong time format! It should be \"DAY.MONTH.YEAR HOURS:MINUTES\"")
        return value


class ReservationOut(BaseModel):
    id: int
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda dt: dt.strftime("%d.%m.%Y %H:%M")
        }
