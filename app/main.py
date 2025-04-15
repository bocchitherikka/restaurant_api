from fastapi import FastAPI

from app.routers.reservations.views import router as reservations_router
from app.routers.tables.views import router as tables_router
from app.services.startup import run_migrations

app = FastAPI()

app.include_router(reservations_router, prefix="/reservations")
app.include_router(tables_router, prefix="/tables")


@app.on_event("startup")
def on_startup():
    run_migrations()


@app.get("/")
def root():
    return {"message": "Hello. Check out README for more info"}
