from pydantic import BaseModel


class DeleteObjectByID(BaseModel):
    id: int
