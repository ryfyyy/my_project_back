from fastapi import APIRouter

from my_project.schemas import StatusResponce

router = APIRouter()

@router.get("/status")
def get_status():
    return StatusResponce(status='ok')

    