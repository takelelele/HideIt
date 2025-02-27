from pydantic import BaseModel
from typing import Optional


class NewSecret(BaseModel):
    secret: str
    passphrase: Optional[str | int] = None

class GetSecret(BaseModel):
    passphrase: Optional[str | int] = None