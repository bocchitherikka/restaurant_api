from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.exceptions import (
    ObjectNotFoundException,
    TableOccupiedException
)

from app.models.reservation import Reservation

from app.dto.general import (
    DeleteObjectByID
)
from app.dto.reservation import (
    ReservationCreate,
    ReservationOut
)

from app.routers.reservations.actions import (
    add_new_reservation_to_db,
    is_the_table_free_at_the_time
)

router = APIRouter()


@router.get(path="/", response_model=list[ReservationOut])
def get_reservations(
        db: Session = Depends(get_db)
):
    reservations = db.query(Reservation).all()
    return reservations


@router.post(path="/")
def create_reservation(
        reservation: ReservationCreate,
        db: Session = Depends(get_db)
):
    if not is_the_table_free_at_the_time(reservation, db):
        raise TableOccupiedException()
    new_reservation = add_new_reservation_to_db(reservation, db)
    return new_reservation


@router.delete(path="/")
def delete_reservation(
        reservation: DeleteObjectByID,
        db: Session = Depends(get_db)
):
    reservation_to_delete = db.query(Reservation).filter(
        Reservation.id == reservation.id
    ).first()
    if reservation_to_delete is None:
        raise ObjectNotFoundException(Reservation)
    db.delete(reservation_to_delete)
    db.commit()
    return {"message": "Reservation deleted successfully"}
