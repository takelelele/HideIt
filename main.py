import uvicorn
from fastapi import FastAPI
from routers import secrets as SecretsRouter
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(SecretsRouter.router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)