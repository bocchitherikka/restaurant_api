from datetime import timedelta
from sqlalchemy.orm import Session

from app.dto.reservation import (
    ReservationCreate
)
from app.models.reservation import Reservation


def is_the_table_free_at_the_time(
        reservation: ReservationCreate,
        db: Session
) -> bool:
    existing_reservations = db.query(Reservation).filter(
        Reservation.table_id == reservation.table_id
    )
    reservation_endtime = (
            reservation.reservation_time +
            timedelta(minutes=reservation.duration_minutes)
    )
    for existing_reservation in existing_reservations:
        exiting_reservation_endtime = (
                existing_reservation.reservation_time +
                timedelta(minutes=existing_reservation.duration_minutes)
        )
        if (
                existing_reservation.reservation_time <=
                reservation.reservation_time <=
                exiting_reservation_endtime
        ) or (
                existing_reservation.reservation_time <=
                reservation_endtime <=
                exiting_reservation_endtime
        ):
            return False
    return True


def add_new_reservation_to_db(
        reservation: ReservationCreate,
        db: Session
) -> Reservation:
    new_reservation = Reservation(
        customer_name=reservation.customer_name,
        table_id=reservation.table_id,
        reservation_time=reservation.reservation_time,
        duration_minutes=reservation.duration_minutes
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation
