from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.exceptions import (
    ObjectNotFoundException,
    TableHasReservationsException
)

from app.models.table import Table

from app.dto.general import (
    DeleteObjectByID
)
from app.dto.table import (
    TableCreate,
    TableOut
)

from app.routers.tables.actions import (
    add_new_table_to_db,
    is_table_has_reservations
)

router = APIRouter()


@router.get("/", response_model=list[TableOut])
def get_tables(
        db: Session = Depends(get_db)
):
    tables = db.query(Table).all()
    return tables


@router.post("/")
def create_table(
        table: TableCreate,
        db: Session = Depends(get_db)
):
    new_table = add_new_table_to_db(table, db)
    return new_table


@router.delete("/")
def delete_table(
        table: DeleteObjectByID,
        db: Session = Depends(get_db)
):
    table_to_delete = db.query(Table).filter(
        Table.id == table.id
    ).first()
    if table_to_delete is None:
        raise ObjectNotFoundException(Table)
    if is_table_has_reservations(table.id, db):
        raise TableHasReservationsException()
    db.delete(table_to_delete)
    db.commit()
    return {"message": "Table deleted successfully"}
