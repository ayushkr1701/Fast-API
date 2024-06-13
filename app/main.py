from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import engine, get_db
from app.exceptions import ConfigurationNotFoundException

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/create_configuration", response_model=schemas.Configuration)
def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_configuration(db, config)

@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)
    if db_config is None:
        raise ConfigurationNotFoundException(country_code)
    return db_config

@app.post("/update_configuration", response_model=schemas.Configuration)
def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, config)
    if db_config is None:
        raise ConfigurationNotFoundException(config.country_code)
    return (config.country_code, "is updated.")

@app.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_configuration(db, country_code)
    if db_config is None:
        raise ConfigurationNotFoundException(country_code)
    return (country_code, "is deleted.")
