from sqlalchemy import exists, func, select
from sqlalchemy.orm import Session

from app.dto.table import TableCreate
from app.models.reservation import Reservation
from app.models.table import Table


def add_new_table_to_db(
        table: TableCreate,
        db: Session
) -> Table:
    new_table = Table(
        name=table.name,
        seats=table.seats,
        location=table.location
    )
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


def is_table_has_reservations(
        table_id: int,
        db: Session
) -> bool:
    query = select(
        exists().where(
            (Reservation.table_id == table_id) &
            (Reservation.reservation_time > func.now()))
    )
    result = db.execute(query).scalar()
    return result
