from fastapi import FastAPI
from app_fast.server.routes.employee import router as EmployeeRouter
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(EmployeeRouter, tags=["Employee"], prefix="/employee")
