from pydantic import BaseModel

class StatusResponce(BaseModel):
    status: str
