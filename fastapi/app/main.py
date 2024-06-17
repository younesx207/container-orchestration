from fastapi import FastAPI
from database.db import initialize_db

#importing routers
import routers.router_items

#api init (launch with uvicorn main:api --reload)
api = FastAPI( 
  title="Items API",
  redoc_url='/'
)

@api.on_event("startup")
async def startup_event():
  initialize_db()

api.include_router(routers.router_items.router)