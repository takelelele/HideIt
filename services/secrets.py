from dto import secrets
from models.secrets import SecretsModel
import uuid


def create_secret(data: secrets.NewSecret, db):
    secret = SecretsModel(id=uuid.uuid4().hex,
                          secret=data.secret,
                          passphrase=data.passphrase)

    try:
        db.add(secret)
        db.commit()
        db.refresh(secret)
    except Exception as e:
        print(e)

    return secret


def get_secret(id: str, data: secrets.GetSecret, db):
    secret = db.query(SecretsModel).filter(SecretsModel.id == id).first()

    if not secret:
        return None

    if secret.passphrase:
        if not data or not data.passphrase or secret.passphrase != data.passphrase:
            return None

    delete_secret(id,db)

    return secret

def delete_secret(id: str, db):
    secret = db.query(SecretsModel).filter(SecretsModel.id==id).first()
    if secret:
        db.delete(secret)
        db.commit()