from fastapi import APIRouter, HTTPException
from App.crud.crud_items import create_item, get_item, filter_items, delete_item, update_item, aggregate_items
from App.models.item import Item
from datetime import datetime

router = APIRouter()


@router.post("/items/", response_model=str, summary="Create a new item")
async def create_item_api(item: Item):
    item_id = await create_item(item)
    return item_id

@router.get("/items/{item_id}", summary="Get an item by ID")
async def get_item_api(item_id: str):
    item = await get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/filter", summary="Filter items based on various criteria")
async def filter_items_api(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    expiry_date = datetime.fromisoformat(expiry_date) if expiry_date else None
    insert_date = datetime.fromisoformat(insert_date) if insert_date else None
    return await filter_items(email, expiry_date, insert_date, quantity)

@router.delete("/items/{item_id}", summary="Delete an item by ID")
async def delete_item_api(item_id: str):
    deleted_count = await delete_item(item_id)
    if deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted successfully"}

@router.put("/items/{item_id}", summary="Update an item by ID")
async def update_item_api(item_id: str, item_data: Item):
    updated_item = await update_item(item_id, item_data.dict(exclude_unset=True))
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.get("/items/aggregate", summary="Aggregate items based on email")
async def aggregate_items_api():
    return await aggregate_items()
