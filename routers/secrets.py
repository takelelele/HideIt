from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from dto.secrets import NewSecret, GetSecret
from services.secrets import create_secret, get_secret

router = APIRouter()

@router.post('/generate')
def create(data: NewSecret = None, db: Session = Depends(get_db)):
    return create_secret(data, db).id

@router.post('/secrets/{id}')
def get(id: str, data: GetSecret = None, db: Session = Depends(get_db)):
    secret = get_secret(id, data, db)
    if secret:
        return secret.secret
    else:
        return "Нет секретов"