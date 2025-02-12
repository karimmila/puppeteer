from fastapi import FastAPI
from app.routes import patient_router
from app.database import engine, Base

def create_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(patient_router, prefix="/api")
