from fastapi import FastAPI
from workout_api.routers import api_router # type: ignore

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)