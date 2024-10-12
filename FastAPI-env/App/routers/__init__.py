# App/routers/__init__.py

# Optional: Import specific routers for easier access
from .items import router as items_router
from .clock_in import router as clock_in_router

# This way, you can access them as:
# from App.routers import items_router, clock_in_router
