import os
from fastapi import FastAPI, APIRouter
from App.routers import items, clock_in


app = FastAPI()
router = APIRouter()


# Include routers
app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(clock_in.router, prefix="/clock_in", tags=["Clock-In Records"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI Project"}


