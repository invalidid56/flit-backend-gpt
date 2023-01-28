from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.generate import generate_router


app = FastAPI()

app.include_router(generate_router.router)
