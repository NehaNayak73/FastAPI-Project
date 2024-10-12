# routers/clock_in.py
from fastapi import APIRouter,HTTPException
from typing import List
from App.models.clockin import ClockInRecord
from App.crud.crud_clockin import create_clockin, get_clockin, filter_clockins, delete_clockin, update_clockin

router = APIRouter()

@router.post("/clock-in", response_model=str)
async def create_new_clockin(clockin: ClockInRecord):
    return await create_clockin(clockin)

@router.get("/clock-in/{clockin_id}", response_model=dict)
async def read_clockin(clockin_id: str):
    return await get_clockin(clockin_id)


@router.delete("/clock_in/clock-in/{clockin_id}")
async def delete_clockin_endpoint(clockin_id: str):
    deleted_count = await delete_clockin(clockin_id)  # Ensure this is not calling the same function
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return {"detail": "Clock-in record deleted successfully"}

@router.put("/clock-in/{clockin_id}", response_model=int)
async def update_clockin_details(clockin_id: str, clockin_data: ClockInRecord):
    return await update_clockin(clockin_id, clockin_data.dict(exclude_unset=True))
