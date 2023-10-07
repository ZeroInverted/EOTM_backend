from fastapi import FastAPI
from routers.employee_router import employee_router
from routers.eotmdetail_router import eotmdetail_router
from routers.collective_router import collective_router
from routers.auth_router import auth_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
eotm = FastAPI()

eotm.include_router(employee_router, prefix="/employee")
eotm.include_router(eotmdetail_router, prefix="/eotmdetail")
eotm.include_router(collective_router, prefix="/collective")
eotm.include_router(auth_router, prefix="/auth")

origins = ["*"]

eotm.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(eotm, port=5555)
