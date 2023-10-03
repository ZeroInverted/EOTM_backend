from fastapi import FastAPI
from routers.employee_router import employee_router
from routers.eotmdetail_router import eotmdetail_router
from fastapi.middleware.cors import CORSMiddleware
store = FastAPI()

store.include_router(employee_router, prefix="/employee")
store.include_router(eotmdetail_router, prefix="'/eotmdetail")


origins = ["*"]

store.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
