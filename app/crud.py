from sqlalchemy.orm import Session
from app.models import Configuration
from app.schemas import ConfigurationCreate, ConfigurationUpdate

def create_configuration(db: Session, config: ConfigurationCreate):
    db_config = Configuration(country_code=config.country_code, config=config.config)
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_configuration(db: Session, country_code: str):
    return db.query(Configuration).filter(Configuration.country_code == country_code).first()

def update_configuration(db: Session, config: ConfigurationUpdate):
    db_config = get_configuration(db, config.country_code)
    if db_config:
        db_config.config = config.config
        db.commit()
        db.refresh(db_config)
        return db_config
    return None

def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
        return db_config
    return None
